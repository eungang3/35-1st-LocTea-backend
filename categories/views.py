from django.http  import JsonResponse
from django.views import View 

from categories.models       import FirstCategory

class CategoryView(View): 
    def get(self, request):
        first_categories = FirstCategory.objects.all()
        result = [{
            'first_category_id' : first_category.id,
            'title'             : first_category.title,
            'second_categories' : [{ 
                'second_category_id': second_category.id,
                'title'             : second_category.title
            } for second_category in first_category.second_categories.all()]
        } for first_category in first_categories]

        return JsonResponse({'result' : result}, status=200)


