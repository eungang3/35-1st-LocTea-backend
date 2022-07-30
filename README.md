# 록차 Loctea (위코드 35기 1차 프로젝트)
- 록차는 오설록 쇼핑몰을 클론코딩한 프로젝트입니다. 
- 개발에 집중하기 위해 기획, 디자인은 참고하고 기능은 직접 구현하였습니다.

<br>

## 1. 선정 이유
1) 멤버십으로 운영되는 사이트 : 회원가입, 로그인, 장바구니 등 인증, 인가 기능을 구현해볼 수 있음
2) 커머스 사이트 : 장바구니, 상품 구매, 주문 관리 기능을 구현해볼 수 있음
3) 다양한 상품 종류와 상세한 카테고리 : 관계형 데이터베이스에 대한 이해도를 높일 수 있음 
4) 다양한 필터링 기능 : django 쿼리에 익숙해질 수 있음

<br>

## 2. 개발 인원
- 백엔드 3명 : 박정용, 조민지, 조예슬
- 프론트엔드 4명 : 김익현, 류승연, 이금관(PM), 최재홍

<br>

## 3. 기간
2022.7.18 ~ 7.29(2주)

<br>

## 4. 백엔드 역할
- 조예슬 : DB 모델링, 카테고리 API, 상품상세API, 상품목록 API, AWS 배포
- 박정용 : DB 모델링, 장바구니 API, 주문배송 API
- 조민지 : DB 모델링, 로그인/회원가입 API, 데코레이터

<br>

## 5. 백엔드 기술 스택
- Back-end : Python, Django, JWT, Bcrypt, Miniconda
- Database : dbdiagram.io, MySQL
- HTTP : Postman
- Common : Trello, Slack, Git & Github

<br>

## 6. API 명세서
https://charmed-skirt-18c.notion.site/API-ad9f438727804f96bec469adebec53cd

<br>

## 7. 시연 영상
https://youtu.be/grWXHlKwkyY
![카테고리_AdobeExpress](https://user-images.githubusercontent.com/47664802/181878541-59376352-15f0-49eb-ab85-9b16bb527efa.gif)
![상품상세_AdobeExpress](https://user-images.githubusercontent.com/47664802/181878546-68374440-c3e5-4c16-9915-28a71d50006a.gif)


<br>

## 8.1 내 역할 - 상품 목록 API 제작

### 구현 사항

- 엔드포인트 : /products/list
- 카테고리 필터, 티 타입별 필터, sorting 구현
- 페이지네이션 구현
- 요청 성공한 경우 : 페이지 정보, 상품 목록과 코드 200 반환
- 요청 실패한 경우 : 존재하지 않는 카테고리나 페이지 요청 시 404 에러 반환

### 배운 점

- 쿼리 파라미터를 이용하여 엔드포인트를 만드는 법에 대해 알게 되었습니다.

- httpie와 포스트맨에서 쿼리 파라미터를 사용하는 법을 알게 되었습니다.

- RESTful의 개념을 익히고 코드에 적용해보았습니다.
   - 처음에는 엔드포인트를 'products/1차 카테고리 아이디/2차 카테고리 아이디'로 작성했습니다.
   - 하지만 products/1/2 같은 URI로는 리소스를 설명할 수 없었습니다.
   - 전체 상품 중 카테고리가 oo번인 상품을 필터링해서 보여준다고 생각하니 더 가독성 있는 엔드포인트를 작성할 수 있었습니다.

- Q 오브젝트에 대해 공부하고 사용해보았습니다.

- 페이지네이션의 원리를 이해하고 구현해보았습니다.

- 복잡해보이는 필터링과 페이지네이션도 글로 정리해보니 하나씩 구현할 수 있었습니다.
   - 어디서부터 시작해야 할 지 모르겠고 막막할 때는 글로 먼저 정리해보는 습관을 들이면 좋을 것 같습니다.


<br>

## 8.2 내 역할 - 상품 상세 API 제작

### 구현 사항

- 엔드포인트 /products/product_id로 요청받습니다.
   - 요청 성공한 경우 : 상품 타이틀, 아이디, 설명, 1차 카테고리명, 2차 카테고리명, 가격, 재고, 할인율, 썸네일 이미지, 상세 이미지 정보를 응답합니다.
   - 요청 실패한 경우 1 : 상품 아이디에 해당하는 상품이 없는 경우 401 에러로 응답합니다.
   - 요청 실패한 경우 2 : 카테고리가 존재하지 않는 경우 401 에러로 응답합니다.

### 배운 점

- 문서화의 중요성을 느꼈습니다. 
   - 처음에는 급한 마음에 API 명세서를 작성하지 않고 구두로 프론트와 커뮤니케이션했습니다.
   - 작업을 진행하다보니 키값이 자꾸 맞지 않아 통신에 어려움이 생겼고, API 명세서를 만들었습니다.
   - 명세서를 작성한 후 작업하니 프론트와 커뮤니케이션이 더 수월해졌고, 스스로도 어떤 기능을 만들어야 하는지 명확하게 정리가 되어 좋았습니다.  

- 패스 파라미터와 쿼리 파라미터의 차이점을 알게되었습니다.
   - 패스 파라미터는 단순히 특정 아이디의 상품을 가져올 때 씁니다.
   - 쿼리 파라미터는 filtering이나 ordering에 더 적절합니다.
   - 해당 api는 그냥 상품 정보를 가져오기 때문에 패스 파라미터를 사용했습니다.

<br>

## 8.3 내 역할 - 카테고리 API 제작

### 구현 사항

- 엔드포인트 /categories로 요청받습니다.
   - 요청 성공한 경우 1 : 모든 1차 카테고리명과 id, 2차 카테고리명과 id를 담은 딕셔너리와 코드 200을 반환합니다.
   - 요청 성공한 경우 2 : 아무 카테고리도 없는 경우 빈 리스트와 코드 200을 반환합니다.

### 배운 점

- 위계를 갖는 데이터는 어떤 구조로 정리해서 보내주어야 프론트에서 사용하기 편할지 고민해보았습니다.
   - 처음에는 카테고리명만 보내주었는데 프론트쪽에서 url을 구성하려면 카테고리 아이디도 필요했습니다.
   - '카테고리 아이디 : 카테고리명'으로 된 키값을 보내주는 경우 가독성이 가장 높고 프론트에서 사용하기도 편리했습니다.

- 리스트 컴프리헨션을 사용했을 때 코드 가독성이 좋아짐을 체감했습니다.

<br>


## 9. DB 모델링
<img width="870" alt="스크린샷 2022-07-29 오후 5 02 46" src="https://user-images.githubusercontent.com/47664802/181713475-dec250ca-5c97-4223-9abf-932c85ef3fef.png">


