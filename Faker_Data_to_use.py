import pandas as pd
from faker import Faker
import random

# set the locale to GB
fake = Faker("en_GB")

# how many customers to fake
N = 50

# get first names, last names and postcodes
first_name = [fake.first_name() for i in range(N)]
last_name = [fake.last_name() for i in range(N)]
office_locations = ["Somerset, NJ","Austin,TX","Piscataway, NJ"]
office = [random.choice(office_locations) for i in range(N)]
email = [first_name[i] + "_" + last_name[i] + "@email.com" for i in range(N)]
sales = [ "$" + str(random.choice(range(1000,1000000))) for i in range(N)]

df_fake = pd.DataFrame({
    "first_name": first_name,
    "last_name": last_name,
    "office": office,
    "email": email,
    "Sales": sales,
    })

print(df_fake)

#Experiement with this for Data Analysis
