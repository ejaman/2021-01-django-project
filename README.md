# 2021-01-django-project
⚠️2021년도 1학기 팀프로젝트<br>
![KakaoTalk_Photo_2021-09-14-11-56-27 001](https://user-images.githubusercontent.com/82802784/133187420-99bd078f-d7d9-471e-bbd5-7fcb2e364c9b.jpeg)

<br><br>
## 소개
+ 코로나시대 생필품을 편리하게 집에서 받아볼 수 있는 배달형 편의점 서비스를 구상했습니다.<br>
+ 이 페이지의 사용자는 관리인으로 로그인해 배달형 편의점의 상품과 재고를 관리합니다.<br>
+ 추가,수정,삭제 등 기본적인 crud 기능을 구현<br>
+ 간단한 자바스크립트로 팝업창과 검색 기능을 추가<br><br>


## 사용한 기술
+ Django(crud)
+ javascript<br><br>


## 담당 파트
+ 템플릿과 html
+ inevntory table & inventory crud
![KakaoTalk_Photo_2021-09-14-11-56-27 002](https://user-images.githubusercontent.com/82802784/133187469-f1fca908-0be6-4840-991b-0a0fc6633bf6.jpeg)
![KakaoTalk_Photo_2021-09-14-11-56-27 003](https://user-images.githubusercontent.com/82802784/133187467-6a554af0-95cf-45f6-b2a3-8b6c29163a08.jpeg)
+ pop up & filtering (javascript)
![KakaoTalk_Photo_2021-09-14-11-56-27 004](https://user-images.githubusercontent.com/82802784/133187462-20a2c9ca-97a1-4745-961c-31904088ab5b.jpeg)

## 고칠점
+ style은 css파일로 만들어서 따로 정리하기
+ 기능 보완




<br><br><br><br>
### 아래는 최종으로 제출한 레포트의 일부입니다.<br>
1.Verified users can check lists of orders and managers on the dashboard page. 
User can update orders on the order list. User can also delete orders after receiving delete confirmation. 
On the manager page, user can create Order and manage Products. User can create, update and delete products on this page. 
It also requires confirmation before delete products. On the Inventory page, user can also do the CRUD actions.

2.First, i made ‘login page’ using Django’s authenticate system.
Django has basically built-in authentication and a User Model itself.
The reason I used this method is that I couldn't create a membership page due to the project setting, which is a site that only administrators can see.

As you can see, you can log in to the database with the new id and pw only with the registered ID and PW.

3.Orders can be placed on the manager's page as the manager's authority. 
We created an order create form to list up to ten input windows using the inlineformset function. 
The same order form is used, but the content included is specified differently by function (update or create) 
and the inline form is used, indicating that the entry form is different from the update.

4.To implement the search function with the 'django_filters.FilterSet' ,
we created filters.py and added it to the manager function of view.py. All other contents of the manager table and the order table are included.

5.*JavaScript When a user update or delete inventory item, the script ‘update/delete id: *’ appears to check one more time.
We failed to link the order table with the inventory table. 
Initially, our plan was made the inventory page automatically modified when the order came in and out, but when the table connecting is failed,
we added a add item page to modify inventory page manually. (initial: if product 카프리썬 is ordered
-> in inventory list, 카프리썬 is automatically added) But for now we can calculate the current amount of inventory.

but we can not automatically add new item on inventory list by order. 
In add page, a pop-up window with a product list and filters has been added so that user can check products before add item on the list(inventory). 
n adding page, the manager should add an order to the add page of the inventory as the concept of approval for one part.
When you select the product name and order, it automatically calculates the current_amount after receiving how many orders were placed.

Filter and filter result

*graph We also try to make visualization part but we couldn’t finish it.
