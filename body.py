class Person:
    def __init__(self,head,tongue):
        self.head = head
        self.tongue = tongue

    def beheading(self):
        if self.head == "green" and self.tongue == "red":
            print ("Person has beheaded")
        else:
            print ("Person remains alive")


person = Person(head="green",tongue="red")
person.beheading()
