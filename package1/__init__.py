import abc

# abc=abstract class


class Animal(abc.ABC):
    def __init(self, name, gender):
        self._name = name
        self._gender = gender

    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def __init__(self, name, gender):
        super().__init__()

    def move(self):
        print("dog moved")

    def eat(self):
        print("dog eated")


class Human(Animal):
    def __init__(self, name, gender, country):
        super().__init__()
        self._country = country

    def move(self):
        print("Human moved")

    def eat(self):
        print("Human eated")

    def speak(self, language):
        self._country = language
        print(f"Human speak {language}!")
