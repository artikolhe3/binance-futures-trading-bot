import logging
from binance.client import Client

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **params):
        logger.info(f"Placing order: {params}")
        try:
            response = self.client.futures_create_order(**params)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.exception("API Error")
            raise
