def app_factory(global_conf, **local_conf):
    return example_app

def example_app(environ, start_response):
    start_response(
        "200 OK",
        [("Content-Type", "text/plain")],
        )
    return ["HELLO ANTEATER, YOU HAVE SUCCEEDED."]    
