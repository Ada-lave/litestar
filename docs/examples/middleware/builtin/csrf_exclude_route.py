@post("/post", exclude_from_csrf=True)
def handler() -> None: ...
