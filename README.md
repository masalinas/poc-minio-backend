# Description
PoC Minio Backend

## Dependencies
```sh
$ pip install flask => Flask Dependency
$ pip install lask-cors => Flask CORD Dependency
$ pip install minio  => minio Dependency
$ pip install urllib3==1.26.6 => remove warning for openssl
```

# Debug Minio

```sh
$ minikube start => start minikube
$ minikube dashboard =A start minikube dashboard
$ kubectl port-forward svc/console -n minio-operator 9090:9090 => port forward for minio operator
$ kubectl port-forward svc/gsdpi-hl -n default 9000:9000 => port forward for minio tenant uniovi
$ source .venv/bin/activate => activate environment for poc-minio-backend
$ python3 job.py => start poc-minio-backend
$ npm run start => start poc-minio-frontend
```