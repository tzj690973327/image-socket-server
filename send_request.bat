curl -X POST -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" -H "Accept: application/json" -F "author=1" -F "title=curl 테스트" -F "text=API curl로 작성된 API 테스트 입력입니다." -F "created_date=2024-06-10T18:34:00+09:00" -F "published_date=2024-06-10T18:34:00+09:00" -F "image=@C:\Users\Shaq\Pictures\1238013.jpg;type=image/jpg" -v http://127.0.0.1:8000