import asyncio
from api_decimal import DecimalChainAPI

api = DecimalChainAPI(limit=10)


async def main():
    address = "0x40900a48273644768c09183e00e43528c17a29f6"
    validator = "0xcad64f9d9ebbd423a9e3d78c36afcf5cfa7fd565"
    contract_address = "0x4E8118E97586A60e5d71e45811E512546bCD52Ce"

    address_info = await api.address_info(address)
    validator_list = await api.validator_list()
    contracts_verification = await api.contracts_verification(contract_address)

    print("Address Info:", address_info)
    print("Validator List:", validator_list)
    print("contracts_verification:", contracts_verification)


if __name__ == "__main__":
    asyncio.run(decimal_api())
