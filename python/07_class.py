class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, I am", self.name)


robot1 = Robot("Akbar Bot")

robot1.say_hello()
