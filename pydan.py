from pydantic import BaseModel,Field
from typing import List , Dict ,Optional,Annotated
class patient(BaseModel):
    name : Annotated[str,Field(max_length=100,title="enter name")]
    age : int
    weight : float = Field(gt=0,lt=100)
    marrige : bool
    allergies : Optional[List[str]]=None
    phoneno : Dict[str,str]
def printdata(pat:patient):
    print(pat.age)
    print(pat.name)
    print(pat.marrige)
    print(pat.allergies)
    print(pat.phoneno)
    print("data stored")

p = {'name':"ghazaal ", "age" : 18,'weight':75,"marrige": False , "allergies":["weak willed men"] , "phoneno":{"email":"ghazaal@gmail"}}
pat= patient(**p)
printdata(pat)

