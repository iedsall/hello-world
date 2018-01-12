print('Find out the name, breed, and color of you new puppy!')
print('Press 1 for name')
print('Press 2 for breed')
print('Press 3 for color')
print('Press number any key to exit')

class Dog():

    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color

dog = Dog(name = 'Sammy', breed = 'Pug', color = 'Brown')
while True:
    userChoice = int(input())
    if userChoice is 1:
        print("His name is: " ,dog.name,"!")
    elif userChoice is 2:
        print("Sammy's breed is: " ,dog.breed)
    elif userChoice is 3:
        print("His color is: " ,dog.color)
    else:
        print("Thanks for messing with me...")
        break
