# from <file> import <Class>
from category import Category


class Store:
    # attributes
    # name
    # categories (departments)
    # constructor - the function that runs every time you create a new instance
    # self refers to the current instance of the class (in JS the word is "this")
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        # return a string repping the store
        output = f"Welcome to {self.name}!"
        i = 1
        for category in self.categories:
            output += f"\n{i}. {category.name}"
            i += 1
        return output

    def __repr__(self):
        # also returns a string
        return f"self.name = {self.name} ; self.categories = {self.categories}"


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Dodgers fans only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "The American kind", [])

sports_store = Store("Gander Mountain", [
                     running_category, baseball_category, basketball_category, football_category])
produce_store = Store("Trader Joe's", ["Dairy", "Meat", "Bread", "Produce"])

print(sports_store)
# print(produce_store)
# print(sports_store.name)
# print(repr(sports_store))


# REPL --> Read Evaluate Print Loop
choice = 0
print("Type Q to Quit")
# while choice != 'q':
#     # READ
#     try:
#         choice = input("Please choose a category (#): ")

#         # EVALUATE
#         chosen_category = sports_store.categories[int(choice)-1]

#         # PRINT
#         print(chosen_category)
#     except (ValueError, IndexError):
#         print("Please enter a valid input")


while True:
    # READ
    try:
        choice = int(input("Please choose a category (#): ")) - 1
        if (choice == 123):  # this won't work because you're subtracting one from the input above
            break
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
        # EVALUATE
        chosen_category = sports_store.categories[choice]

        # PRINT
        print(chosen_category)
    except (ValueError, IndexError):
        print("Please enter a valid input")
