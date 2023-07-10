#Marcus Lauber, July 9th 2023
#Program defining a class (flower) using the constructor method. The class has three methods. The first define a name variable to name objects. The second relates to the real life action of a flower growing and outputs "the (name of flower) is growing". The the third method for the flower class, relates to the real life action of a flower blooming and outputs "the (name of flower" is blooming". Then, the  program defines the function "main" to create three objects with the titles of "Rose","Daisy",and "Tulip". The main function then uses the grow and blow method from the flower class after defining each object. Lastly the program runs the "main" function.
class Flower:
    def __init__(self, name):
        self.name = name

    def grow(self):
        print("The " +self.name + " is growing.")

    def bloom(self):
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose")
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Tulip")
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":
  main()