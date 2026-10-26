class Hero:
    def __init__(self,name, hero_class,hp,attack):
        self.name = name
        self.hero_class = hero_class
        self.hp = hp
        self.attack = attack
        print("Галк вийшов на поле бою")
    def say_hello(self):
        print(f"Привіт! Я {self.name}")

HULK = Hero("Галк", "Силач", 400, 350)
HULK.say_hello()