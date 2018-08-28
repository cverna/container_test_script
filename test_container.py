import conu

IMAGE = "registry.fedoraproject.org/f27/tools"
TAG = "latest"
PORT = 5000


with conu.DockerBackend() as backend:
    image = backend.ImageClass("flaskapp_container")
    options = ["-p", "5000:5000"]
    container = image.run_via_binary(additional_opts=options)

    try:
        assert container.is_running()

        container.wait_for_port(PORT)
        http_response = container.http_request(path="/", port=PORT)
        assert http_response.ok
        assert "Hello Container World!" in http_response.content.decode("utf-8")

        logs = [line for line in container.logs()]
        assert b'"GET / HTTP/1.1" 200 -' in logs[-1]

    finally:
        container.stop()
        container.delete()
