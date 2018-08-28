FROM registry.fedoraproject.org/fedora-minimal:latest

RUN microdnf -y install python3-flask && microdnf clean all
ADD ./app.py /srv

CMD ["python3", "/srv/app.py"]
