

#define my favorite animal (cats!) as a class
class Cat:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        # Initialize the data members
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_physical_characteristics(self):
        # Print out and describe the physical characteristics of the cat
        print(f"Physical Characteristics of the Cat:")
        print(f"Arm Length: {self.arm_length} feet")
        print(f"Leg Length: {self.leg_length} feet")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")


#Cat class with specific physical characteristics
my_cat = Cat(0.5, 0.8, 2, True, True)

# describe the physical characteristics
my_cat.describe_physical_characteristics()
