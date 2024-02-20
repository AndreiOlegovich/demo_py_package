def url_gen(service: str) -> str:
    service_dict = {"hosting": "https://beget.com"}
    if service in service_dict:
        return service_dict(service)
    else:
        return "Unknown service"
