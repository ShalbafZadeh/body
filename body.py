class Person:

    def __init__(self, head, tounge):
        self.head = head
        self.tounge = tounge

    def beheading(self):
        if self.head == "green" and self.tounge == "red":
            print ("Person is going to be beheaded")
        else:
            print ("Person remains alive")


person = Person(head="green", tounge="red")
person.beheading()

