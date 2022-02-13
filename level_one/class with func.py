class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender
    #Функції класу
    #функція повертає імя. Атрибути або методи
    #класу можна викликати використовуючи ключове слово self
    def get_name(self):
        return self.name
    def get_age_and_name(self):
        return self.age, self.get_name()


human_1 = Human(age=25, name = 'John', gender='male')
#буде виведено кортеж (25, 'John' )
print (human_1.get_age_and_name())