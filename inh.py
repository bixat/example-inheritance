class info:
    def __init__(self,name,age,country):
        self.var_name = name
        self.var_age = age
        self.var_country = country
    def name(self):
        print('Name : '+self.var_name)

    def age(self):
        print('Age : '+str(self.var_age))

    def country(self):
        print('Country : '+self.var_country)

class infoschool:
    def __init__(self,bac,bac_2,bac_3):
        self.var_bac = bac
        self.var_bac_2 = bac_2
        self.var_bac_3 = bac_3
    def bac(self):
        print('Bac : '+self.var_bac)

    def bac_2(self):
        print('Bac+2 : '+str(self.var_bac_2))

    def bac_3(self):
        print('Bac+3 : '+self.var_bac_3)

class cv(info,infoschool):
    def __init__(self,name,age,country,bac,bac_2,bac_3):
        info.__init__(self,name,age,country)
        infoschool.__init__(self,bac,bac_2,bac_3)

CVIN = cv('Mohammed',21,'MOROCCO','LETTER','MANAGEMENT','MONP')
CVIN.bac_3()
CVIN.name()