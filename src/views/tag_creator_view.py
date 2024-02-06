from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # business rule logic
        print("estou na minha view")
        print(product_code)
        # return http
        return HttpResponse(status_code=200, body={"Hello": "world"})
