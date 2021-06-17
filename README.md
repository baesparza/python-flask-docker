# python-flask-docker

## Run Project

```sh
python3 -m flask run
```

## Pull and run container
```sh
docker pull baesprza/practica-dockerizacion-python

docker run \
    -d --rm \
    --name bruno-python \
    -p 5000:5000 \
    baesprza/practica-dockerizacion-python
```
