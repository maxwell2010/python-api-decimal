import aiohttp
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class DecimalChainAPI:
    BASE_URL = "https://api.decimalchain.com/api/v1"

    def __init__(self, limit=50, offset=0):
        self.limit = limit
        self.offset = offset

    async def get_data(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}?limit={self.limit}&offset={self.offset}"
        print(url)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        ok = data.get("ok", data.get("Ok", False))
                        result = data.get("result", data.get("Result", None))
                        if ok and result is not None:
                            return result
                        else:
                            logging.error(f"Unexpected response structure: ok={ok}, result={result}")
                            return None
                    else:
                        logging.error(f"Request failed with status: {response.status}")
                        return None
            except aiohttp.ClientError as e:
                logging.error(f"Client error occurred: {e}")
                return None
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                return None

    async def post_data(self, endpoint, payload=None):
        url = f"{self.BASE_URL}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload) as response:
                    if response.status == 200:
                        data = await response.json()
                        ok = data.get("ok", data.get("Ok", False))
                        result = data.get("result", data.get("Result", None))
                        if ok and result is not None:
                            return result
                        else:
                            logging.error(f"Unexpected response structure: ok={ok}, result={result}")
                            return None
                    else:
                        logging.error(f"Request failed with status: {response.status}")
                        return None
            except aiohttp.ClientError as e:
                logging.error(f"Client error occurred: {e}")
                return None
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                return None

    # address
    async def address_list(self):
        endpoint = f"addresses/"
        return await self.get_data(endpoint)

    async def address_count(self):
        endpoint = f"addresses/count"
        return await self.get_data(endpoint)

    async def address_live(self):
        endpoint = f"addresses/live"
        return await self.get_data(endpoint)

    async def address_balances(self, address):
        endpoint = f"addresses/{address}/balances"
        return await self.get_data(endpoint)

    async def address_coins(self, address):
        endpoint = f"addresses/{address}/coins"
        return await self.get_data(endpoint)

    async def address_info(self, address):
        endpoint = f"addresses/{address}/info"
        return await self.get_data(endpoint)

    async def address_is_updated(self, address):
        endpoint = f"addresses/{address}/is-updated"
        return await self.get_data(endpoint)

    async def address_stakes_delegated(self, address):
        endpoint = f"addresses/{address}/stakes/delegated"
        return await self.get_data(endpoint)

    async def address_stakes_redelegating(self, address):
        endpoint = f"addresses/{address}/stakes/redelegating"
        return await self.get_data(endpoint)

    async def address_stakes_undelegating(self, address):
        endpoint = f"addresses/{address}/stakes/undelegating"
        return await self.get_data(endpoint)

    async def address_txs(self, address):
        endpoint = f"addresses/{address}/txs"
        return await self.get_data(endpoint)

    async def address_id(self, address_id):
        endpoint = f"addresses/{address_id}"
        return await self.get_data(endpoint)

    # validator
    async def validator_live(self):
        endpoint = f"validators/live"
        return await self.get_data(endpoint)

    async def validator_select(self):
        endpoint = f"validators/validators-select"
        return await self.get_data(endpoint)

    async def validator_validators(self, validator):
        endpoint = f"validators/validators/{validator}"
        return await self.get_data(endpoint)

    async def address_stakes_coins(self, address):
        endpoint = f"validators/wallet/{address}/stakes/coins"
        return await self.get_data(endpoint)

    async def address_stakes_nfts(self, address):
        endpoint = f"validators/wallet/{address}/stakes/nfts"
        return await self.get_data(endpoint)

    async def validator_stakes_coins(self, validator):
        endpoint = f"validators/{validator}/stakes/coins"
        return await self.get_data(endpoint)

    async def validator_stakes_nft(self, validator):
        endpoint = f"validators/{validator}/stakes/nfts"
        return await self.get_data(endpoint)

    async def validator_transfer_coins(self, validator):
        endpoint = f"validators/{validator}/transfer/coins"
        return await self.get_data(endpoint)

    async def validator_transfer_nft(self, validator):
        endpoint = f"validators/{validator}/transfer/nfts"
        return await self.get_data(endpoint)

    async def validator_unstakes_coins(self, validator):
        endpoint = f"validators/{validator}/unstakes/coins"
        return await self.get_data(endpoint)

    async def validator_unstakes_nft(self, validator):
        endpoint = f"validators/{validator}/unstakes/nfts"
        return await self.get_data(endpoint)

    # block
    async def blocks(self):
        endpoint = f"blocks/blocks"
        return await self.get_data(endpoint)

    async def blocks_latest(self):
        endpoint = f"blocks/latest"
        return await self.get_data(endpoint)

    async def blocks_live(self):
        endpoint = f"blocks/live"
        return await self.get_data(endpoint)

    async def blocks_height(self, height):
        endpoint = f"blocks/{height}"
        return await self.get_data(endpoint)

    async def blocks_evm(self):
        endpoint = f"blocks/blocks/evm-blocks"
        return await self.get_data(endpoint)

    async def blocks_evm_height(self, height):
        endpoint = f"blocks/blocks/evm-blocks/{height}"
        return await self.get_data(endpoint)

    # txs
    async def txs_check_tx(self):
        endpoint = f"txs/check-tx"
        return await self.get_data(endpoint)

    async def txs_drc20(self):
        endpoint = f"txs/drc20"
        return await self.get_data(endpoint)

    async def txs_live(self):
        endpoint = f"txs/live"
        return await self.get_data(endpoint)

    async def txs_txs(self):
        endpoint = f"txs/txs"
        return await self.get_data(endpoint)

    async def txs_by_address(self, address):
        endpoint = f"txs/txs-by-address/{address}"
        return await self.get_data(endpoint)

    async def txs_by_block(self, height):
        endpoint = f"txs/txs-by-block{height}"
        return await self.get_data(endpoint)

    async def txs_by_hash(self, hash_tx):
        endpoint = f"txs/txs-by-hash{hash_tx}"
        return await self.get_data(endpoint)

    # rewards
    async def rewards_live(self):
        endpoint = f"rewards/live"
        return await self.get_data(endpoint)

    async def rewards_by_validator(self, validator):
        endpoint = f"rewards/rewards-by-validator/{validator}"
        return await self.get_data(endpoint)

    async def rewards_by_validator_total(self, validator):
        endpoint = f"rewards/rewards-by-validator/{validator}/total"
        return await self.get_data(endpoint)

    async def rewards_address(self, address):
        endpoint = f"rewards/{address}"
        return await self.get_data(endpoint)

    async def rewards_address_total(self, address):
        endpoint = f"rewards/{address}/total"
        return await self.get_data(endpoint)

    # contracts
    async def contracts(self):
        endpoint = f"contracts/"
        return await self.get_data(endpoint)

    async def contracts_live(self):
        endpoint = f"contracts/live"
        return await self.get_data(endpoint)

    async def contracts_compact(self, address):
        endpoint = f"contracts/compact/{address}"
        return await self.get_data(endpoint)

    async def contracts_address(self, address):
        endpoint = f"contracts/{address}"
        return await self.get_data(endpoint)

    async def contracts_verification(self, address):
        endpoint = f"contracts/{address}/verification"
        return await self.post_data(endpoint)

    # NFTs
    async def nft_live(self):
        endpoint = f"nfts/live"
        return await self.get_data(endpoint)

    async def nft_collections(self):
        endpoint = f"nfts/collections"
        return await self.get_data(endpoint)

    async def nft_addresses_tokens(self, address):
        endpoint = f"nfts/addresses/{address}/tokens"
        return await self.post_data(endpoint)

    async def nft_addresses_transfers(self, address):
        endpoint = f"nfts/addresses/{address}/transfers"
        return await self.post_data(endpoint)

    async def nft_collections_address(self, address):
        endpoint = f"nfts/collections/{address}"
        return await self.get_data(endpoint)

    async def nft_collections_tokens(self, address):
        endpoint = f"nfts/collections/{address}/tokens"
        return await self.get_data(endpoint)

    async def nft_collections_transfers(self, address):
        endpoint = f"nfts/collections/{address}/transfers"
        return await self.get_data(endpoint)

    async def nft_token_id(self, address, token_id):
        endpoint = f"nfts/token/{address}/{token_id}"
        return await self.get_data(endpoint)

    async def nft_token_id_transfers(self, address, token_id):
        endpoint = f"nfts/token/{address}/{token_id}/transfers"
        return await self.get_data(endpoint)
