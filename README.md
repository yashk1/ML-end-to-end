# ML-end-to-end

Full deployment of machine learning project

## Requirements

1. Github
2. Heroku
3. VS code
4. Git CLI

## Creating Conda env

```
conda create -p venv 
```

## Activate conda

```
conda activate penv
```

## Create requirements.txt

```
#install requirements
pip install -r requirement.txt

```

# Git Commands

To check all version maintained by git

```
git log
```

To create version/ commit all files

```
git commit -m "message"
```

To send version/changes to git

```
git push origin main
```

To check remote url

```
git remote -v
```

# Heroku

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = yash95kumar@gmail.com
2. HERKOU_API_KEY = c5770b8f-2de5-4fba-a42b-718d2a5e6e3a
3. HEROKU_APP_NAME = ml-regression-basic

# Docker

Build Docker image

```
docker build -t <image-name>:<tagname> .
```

> Note: Image name for docker must be lowercase

To list docker images

```
docker images
```

Run docker image

```
docker run -p 4000:4000 -e PORT=4000 e34831e5210e
```

To check running containers

```
docker ps
```

To stop docker coantainer

```
docker stop <container-id>
```

Remove a container
