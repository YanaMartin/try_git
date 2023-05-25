"""first you have to cd the repo you want to set git in. for exampl: cd desktop/practice/try_git."""

yanas-MacBook-Air:try_git yanakirilov$ git init
#Initialized empty Git repository in /Users/yanakirilov/Desktop/practice/try_git/.git/
yanas-MacBook-Air:try_git yanakirilov$ git add . """the . adds all files in the repo, for 1 file use the name"""
yanas-MacBook-Air:try_git yanakirilov$ git status
#On branch master

#No commits yet

#Changes to be committed:
#  (use "git rm --cached <file>..." to unstage)

#        new file:   to_do.py

yanas-MacBook-Air:try_git yanakirilov$ git commit -m "first commit"
#[master (root-commit) c113047] first commit
# 1 file changed, 24 insertions(+)
# create mode 100644 to_do.py
yanas-MacBook-Air:try_git yanakirilov$ git remote add origin https://github.com/YanaMartin/try_git.git
yanas-MacBook-Air:try_git yanakirilov$ git branch -M main
yanas-MacBook-Air:try_git yanakirilov$ git push -u origin main
#Enumerating objects: 3, done.
#Counting objects: 100% (3/3), done.
#Delta compression using up to 4 threads
#Compressing objects: 100% (2/2), done.
#Writing objects: 100% (3/3), 514 bytes | 514.00 KiB/s, done.
#Total 3 (delta 0), reused 0 (delta 0)
#To https://github.com/YanaMartin/try_git.git
# * [new branch]      main -> main
#Branch 'main' set up to track remote branch 'main' from 'origin'.

"""now i made a change"""
yanas-MacBook-Air:try_git yanakirilov$ git status 
#On branch main
#Your branch is up to date with 'origin/main'.

#Changes not staged for commit:
#  (use "git add <file>..." to update what will be committed)
#  (use "git checkout -- <file>..." to discard changes in working directory)

#        modified:   to_do.py

#no changes added to commit (use "git add" and/or "git commit -a")

"""upload the changed file"""
yanas-MacBook-Air:try_git yanakirilov$ git add to_do.py
yanas-MacBook-Air:try_git yanakirilov$ git commit -m "added new task"
#[main 61bbe49] added new task
# 1 file changed, 1 insertion(+)
yanas-MacBook-Air:try_git yanakirilov$ git push -u origin main
#Enumerating objects: 5, done.
#Counting objects: 100% (5/5), done.
#Delta compression using up to 4 threads
#Compressing objects: 100% (2/2), done.
#Writing objects: 100% (3/3), 288 bytes | 288.00 KiB/s, done.
#Total 3 (delta 1), reused 0 (delta 0)
#remote: Resolving deltas: 100% (1/1), completed with 1 local object.
#To https://github.com/YanaMartin/try_git.git
#   c113047..61bbe49  main -> main
#Branch 'main' set up to track remote branch 'main' from 'origin'.