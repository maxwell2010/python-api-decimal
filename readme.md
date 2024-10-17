## Данные методы были организованы в одном файле для удобства доступа при написании сервисов на языке python


## На текущий момент в прод окружении есть следующие новые API:

Block Service - 
https://api.decimalchain.com/api/v1/blocks/docs/index.html

Transaction Service - 
https://api.decimalchain.com/api/v1/txs/docs/index.html

Reward Service - 
https://api.decimalchain.com/api/v1/rewards/docs/index.html

Coin Service - 
https://api.decimalchain.com/api/v1/coins/docs/index.html

Contract Service - 
https://api.decimalchain.com/api/v1/contracts/docs/index.html

NFT Service - 
https://api.decimalchain.com/api/v1/nfts/docs/index.html

Validator Service - 
https://api.decimalchain.com/api/v1/validators/docs/index.html

Address Service - 
https://api.decimalchain.com/api/v1/addresses/docs/index.html

Это прод окружение
Те же самы свагеры для тест окружений доступны по тем же URL, но только с приставкой testnet-

Например, Block Service - https://testnet-api.decimalchain.com/api/v1/blocks/docs/index.html

Спасибо команде Decimal за предоставленные свагеры

# Взаимодействие:

```python
import asyncio
from api_decimal import DecimalChainAPI

api = DecimalChainAPI(limit=10)


async def main():
    address = "0x40900a48273644768c09183e00e43528c17a29f6"
    validator = "0xcad64f9d9ebbd423a9e3d78c36afcf5cfa7fd565"
    contract_address = "0x4E8118E97586A60e5d71e45811E512546bCD52Ce"

    address_info = await api.address_info(address)
    validator_select = await api.validator_select()
    contracts_verification = await api.contracts_verification(contract_address)

    print("Address Info:", address_info)
    print("Validator List:", validator_select)
    print("contracts_verification:", contracts_verification)


if __name__ == "__main__":
    asyncio.run(decimal_api())
```
