class Insect:
    def __init__(self, name, wings):
        self.__name = name
        self.__wings = wings

    def set_name(self, name):
        self.__name = name

    def set_wings(self, wings):
        self.__wings = wings

    def get_name(self):
        return self.__name

    def get_wings(self):
        return self.__wings


class Bumblebee(Insect):
    def __init__(self, name, wings, color):
        super().__init__(name, wings)
        self.__color = color

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def fly(self):
        print(f"The {self.get_color()} bumblebee is buzzing and flying around.")

    def collect_nectar(self):
        print(f"The {self.get_color()} bumblebee is collecting nectar from a flower.")


class Grasshopper(Insect):
    def __init__(self, name, wings, jump_height):
        super().__init__(name, wings)
        self.__jump_height = jump_height

    def set_jump_height(self, jump_height):
        self.__jump_height = jump_height

    def get_jump_height(self):
        return self.__jump_height

    def hop(self):
        print(f"The {self.get_name()} grasshopper is hopping {self.get_jump_height()} feet in the air.")

    def chirp(self):
        print(f"The {self.get_name()} grasshopper is chirping loudly to attract a mate.")

    # create instances of Bumblebee and Grasshopper
bb = Bumblebee("Bumblebee", 2, "yellow and black")
gh = Grasshopper("Green Grasshopper", 4, 3)

# call methods to demonstrate characteristics
bb.fly()
bb.collect_nectar()
gh.hop()
gh.chirp()

