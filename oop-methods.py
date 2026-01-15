class Doctor:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__format_names()


    def __format_names(self):
        self.firstname = self.firstname.title()
        self.lastname = self.lastname.title()

    def introduce(self):
        print (f"I am {self.firstname}")

    # def __str__(self):
    #     return f"Doctor: {self.firstname} {self.lastname}"
    

doc_sai = Doctor("Sai","shiridi")
doc_venkayya = Doctor("venkayya", "golagamudi")
doc_sai.introduce()
doc_venkayya.introduce()
print(doc_sai)
print(doc_venkayya)
