from coinbase_commerce.api_resources.base import CreateAPIResource
from coinbase_commerce.api_resources.base import DeleteAPIResource
from coinbase_commerce.api_resources.base import ListAPIResource
from coinbase_commerce.api_resources.base import UpdateAPIResource
from coinbase_commerce.util import register_resource_cls
from coinbase_commerce import util


@register_resource_cls
class Invoice(ListAPIResource,
              CreateAPIResource,
              DeleteAPIResource):
    RESOURCE_PATH = "invoices"
    RESOURCE_NAME = "invoice"

    @classmethod
    def void(cls, entity_id, **params):
        response = cls._api_client.put(
            cls.RESOURCE_PATH, entity_id, 'void',
            data=params
        )
        return util.convert_to_api_object(response, cls._api_client, cls)
