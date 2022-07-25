from django.http           import JsonResponse
from django.views          import View
from django.db.models      import Q
from django.core.paginator import Paginator

from products.models    import Product

class ProductListView(View):
    def get(self, request):
        limit              = request.GET.get("limit", 10)
        offset             = request.GET.get("offset", 1)
        first_category_id  = request.GET.get('first-category')
        second_category_id = request.GET.get('second-category')
        sort               = request.GET.get('sort')
        tea_types          = request.GET.getlist('type')

        queries  = Q(second_category__first_category_id = 1)

        if first_category_id:
            queries = Q(second_category__first_category_id = first_category_id)

        if second_category_id:
            queries = Q(second_category = second_category_id)

        if tea_types:
            tea_type_queries = Q()
            tea_type_queries |= Q(types__name__in = tea_types)
            queries &= tea_type_queries

        sort_dict = {
            'price-desc' : '-price', 
            'price-asc'  : 'price' 
        }
        ordering = sort_dict.get(sort, '-created_at')

        products = Product.objects.filter(queries).order_by(ordering).distinct()
        
        p = Paginator(products, limit)
        pages_count = p.num_pages

        if offset < 1 or offset > pages_count:
            return JsonResponse({'result': 'INVALID_PAGE'}, status=404)

        total = {
            'total_items' : products.count(),
            'total_pages' : pages_count,
            'current_page': offset,
            'limit'       : limit
            }
        
        result = []
        page_items = p.page(offset) 
        for page_item in page_items:
            result.append({
                'id'              : page_item.id,
                'title'           : page_item.title,
                'price'           : page_item.price,
                'stock'           : page_item.stock,
                'thumbnail_images': [image.url for image in page_item.thumbnail_images.all()],
                'types'           : [type.name for type in page_item.types.all()]
            })

        return JsonResponse({'total' : total, 'result': result}, status=200)
        
