import looker_sdk

from looker_sdk.sdk.api40.methods import Looker40SDK

sdk: Looker40SDK = looker_sdk.init40()

response = sdk.run_look(
    look_id=str(64),  # Converta o ID para string
    result_format="csv"  # Formato desejado

)
print(response)