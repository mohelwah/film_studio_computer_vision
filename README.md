[![Python application test with Github Actions](https://github.com/mohelwah/film_studio_computer_vision/actions/workflows/main.yml/badge.svg)](https://github.com/mohelwah/film_studio_computer_vision/actions/workflows/main.yml)

# film_studio_computer_vision

## Prepare aws code9:
- generate ssh key to conncet to github 'ssh-keygen -t rsa'.
- cat the public key ' cat /home/ec2-user//.ssh/id_rsa.pub'.
- add ssh key to github account.
- copy your repo to code9 'git clone git@github.com:mohelwah/film_studio_computer_vision.git'.


## create scafold:
- cd to main project folder 
- create vene by 'python3 -m venv ~/.film_studio'.
- activate venv 'source ~/.film_sudio/bin/activate'
- Makefile 'touch Makefile'
- Requriments 'touch requeriments'
- make a hello file 'touch hello.py'

- add install line in makefile and add pack in  requeriments 