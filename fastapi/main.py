from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel, Field


class ShopInfo(BaseModel):
  name:str
  location:str

class Item(BaseModel):
  name:str = Field(min_length=4,max_length=12)
  description:Optional[str] = None
  price:int
  tax:Optional[float] = None

class Data(BaseModel):
  shop_Info:Optional[ShopInfo] = None
  item:List[Item]

app = FastAPI()

'''
想定されるデータ例
{
  "name":"test",
  "description":"test_test",
  "price":5980,
  "tax":1.1
}
'''
@app.post("/")
async def index(data:Data):
  message = {"data":data}
  return message


@app.post("/item/")
async def create_Item(item:Item):
  message = {"message":f"{item.name}は、税込価格{int(item.price*item.tax)}円です。"}
  return message



# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

# http://127.0.0.1:8000/countries/?country_name=japan&country_no=7
# http://127.0.0.1:8000/countries/japan?city_name=tokyo
# @app.get("/countries/")
# async def country(country_name: Optional[str] = None , country_no: Optional[int] = None):
#     return {
#         "country_name":country_name,
#         "country_no":country_no
#     }

# @app.get("/countries/japan")
# async def countries_japan():
#     return {"message":"This is japan"}

# @app.get("/countries/{country_name}")
# async def countries(country_name:str):
#     return {"country_name":country_name}
