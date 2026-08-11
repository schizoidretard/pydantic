from pydantic import BaseModel, field_validator , model_validator , computed_field
from typing import Dict,List
class Patient(BaseModel):
    name: str
    age: int
    weight : int
    height : int
    marrige: bool
    contact : Dict[str,str]
    
   
    @field_validator("name")
    @classmethod
    def transformanme(cls,val):
        val = val.upper()
        return val
    @model_validator( mode="after")
    @classmethod
    def addcontact(cls,model):
        if model.age > 60:
            model.contact.update({"emergency":"03084939223"})
        return model
    @computed_field
    @property
    def calcbmi(self)-> float:
        bmi = self.weight*(self.height/2)
        return bmi



  

    def printinfo(self):
        print(self.age)
        print(self.marrige)
        print(self.name)
        print(self.contact)
        print(self.calcbmi)

# Example usage
p = {"name": "ghazaal", "age": 61,"weight":75,"height":186, "marrige": False , "contact":{"email":"ghazaal@gmail.com", "phone num":"03024545319"}}
pat = Patient(**p)
pat.printinfo()
