def demo_function(service: str) -> str:
    service_dict = {
            "hosting": "https://beget.com"
            "tickets": "https://aviasales.com"
    }
    if service in service_dict:
        return f"Recommended service for {service} is {service_dict[service]}"
    else:
        return "Unknown service"
