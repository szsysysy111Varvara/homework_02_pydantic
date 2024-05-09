from pydantic import BaseModel, conint, EmailStr, constr, field_validator, ValidationError

class Address(BaseModel):
    city: constr(min_length=2)
    street: constr(min_length=3)
    house_number: conint(gt=0)

class User(BaseModel):
    name: constr(min_length=2)
    age: conint(ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @classmethod
    def get_json(cls, json_str):
        try:
            user_data = cls.parse_raw(json_str)
            return user_data.json()
        except ValidationError as error:
            return f"ValidationError: {error}"

    @field_validator('age')
    def check_age(cls, age, values):
        if age > 120 and values.get('is_employed'):
            raise ValueError("Age must be less than 120 years old.")

users_data = [
    {
        "name": "John",
        "age": 30,
        "email": "john@example.com",
        "is_employed": True,
        "address": {
            "city": "Konstanz",
            "street": "Hauptstr. 32",
            "house_number": 55
        }
    },
    {
        "name": "Alissia",
        "age": 130,
        "email": "alissia@example.com",
        "is_employed": True,
        "address": {
            "city": "Milano",
            "street": "Stritto 3",
            "house_number": 2
        }
    },
    {
        "name": "Alex",
        "age": 26,
        "email": "alex@example.com",
        "is_employed": False,
        "address": {
            "city": "Triberg",
            "street": "Volks 67",
            "house_number": 45
        }
    }
]

for user_data in users_data:
    try:
        user = User(**user_data)
        print(user_data)
    except ValidationError as error:
        print(f"ValidationError: {error}")
    print()






