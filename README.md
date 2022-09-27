# github 


### repository 생성
git을 설치하고, github에서 new repository를 생성한다.

터미널에서  
>`git config --global user.name "본인의username"`을 입력한다.  
>`git config --global user.email "본인의email"`을 입력한다.

  
### github 원격저장소 복제(clone)
>만든 repository와 clone할 파일로 이동한다. (윈도우환경 --> `cd`이용)  
>`git clone "https://github.com/moom2ng...."` repository의 url을 복사 붙여넣기하여 해당 폴더를 clone으로 만든다.   

  
### git add, commit, push
repository 이름(ex.test)로 경로를 이동한다 : `cd test`  
해당 폴더에 작업한 파일(document.txt)을 두고 `git status`를 하면 untracked files에 document.txt가 있음을 알 수 있다.  
  
- git add  
> `git add document.txt`를 하면 document파일이 staging area로 이동하게 되어 commit할 준비가 된다.  
> `git add`뒤에 그냥 `.`이나 `*`를 붙이면 해당 폴더에 있는 모든 파일을 add하게 된다.  
  
- git commit  
> 파일을 git repository로 이동  
> 예시, `git commit -m "Add text file [document]"`  
> `-m` : 메시지 입력  

- git push  
> `git push` : clone된 github repository에 파일이 업로드 됨을 확인할 수 있다.

  
### branch
`git branch`를 통해 현재의 브랜치위치와 브랜치 종류를 확인할 수 있다.  

- branch 추가하기  
> `git branch develop` : develop이란 branch추가  

- branch 제거하기  
> `git branch -D develop` : develop이란 branch제거  

- 현재 branch 위치 변경하기  
> *현재 branch 위치가 develop이 아니라고 가정*  
> `git checkout develop` : devlop이란 branch로 이동  


### branch 합치기
**main branch에서 업로드한 a라는 파일을 develop branch에서 a파일을 수정했을 경우*  

develop branch에서 `git add`, `git commit` 진행  
`git log`를 실행해보면, 변경된 사항의 HEAD는 develop을 가리키고 있고 깃허브 원격저장소는 변경사항이 없음을 확인할 수 있다.  
즉, 깃허브는 그대로이다.  
*(log에서 나갈 때 키보드의 **Q**를 누르면 빠져나간다)*  

`git checkout main` : main branch로 이동  
그 다음 `git merge develop`을 진행하면 `git log`를 통해 HEAD가 main과 develop 둘 다 가리키고 있음을 확인할 수 있다.  
그다음 `git push`를 진행하면 a파일의 변경사항이 적용된 파일이 깃허브 원격저장소에 업로드된다.  


### error  
![error_img]

#### 참고자료
git원리사용 원리 이해하는데 도움 : <https://youtu.be/Z9dvM7qgN9s>  
window바탕의 실습 내용 많음 : <https://youtu.be/rhP5pseOJc0>  
