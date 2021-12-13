"""
ID|name|DOB|Gender|Age|Zip code|Amount

1000|John Smith |01/01/2000|F|20|08122-2324|1500.20

2000|Jim McDonald |02/02/2020|M|25|08136-2324|1500.20

20|Jim McDonald|02/02/1999|M|25|08124-6565|1500.20

"""

class details:

    def __init__(self,i,n,d,g,a,z,am):

        self.id=i
        self.name=n
        self.dob=d
        self.gender=g
        self.age=a
        self.zipcode=z
        self.amount=am
       


obj1=details(1000,"johnsmith","01/01/2000","female","20","08122-2324","1500.20")
obj2=details(2000,"jim McDonald","02/02/2020","male","25","08136-2324","1500.20")
obj3=details(20,"jim McDonald","02/02/1999","male","25","08124-6565","1500.20")

k="obj1","obj2","obj3"

print(k)

