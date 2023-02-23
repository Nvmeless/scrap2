class StudyramaEntry:
    def __init__(self,title,name,adress,realAdress,departement,country,tel,email):
        
        self.setTitle(title)
        self.name = name
        self.setAdress(adress)
        self.realAdress = realAdress
        self.departement = departement
        self.country = country
        self.tel = tel
        self.setEmail(email)
        self.password = "azerty"

    def setTitle(self, title):
        self.title = title.replace('- Studyrama', "")
    def setAdress(self, arrAdress):
        self.adress = " ".join(arrAdress)
    def getDictEntry(self):
        return {
            "title":self.title,
            "name":self.name,
            "adress":self.adress,
            "realAdress":self.realAdress,
            "departement":self.departement,
            "country":self.country,
            "tel":self.tel,
            "email":self.email
        }

    def setEmail(self, newEmail):
        self.email = newEmail

    def getPassword(self):
        return "*" * len(self.password)

    def setPassword(self, oldPassword, newPassword):
        if oldPassword == self.password:
            self.password = newPassword
            print("Password Changed")
        else:
            print('Not The Motdepasse')