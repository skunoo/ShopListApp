class GroceryList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("The item is not in the list.")

    def modify_item(self, old_item, new_item):
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item
        else:
            print("The item to modify is not in the list.")

    def show_list(self):
        print(f"Grocery list '{self.name}':")
        for item in self.items:
            print("- " + item)


def main():
    grocery_list = GroceryList("Weekly Shopping")

    grocery_list.add_item("Bread")
    grocery_list.add_item("Milk")
    grocery_list.add_item("Fruits")

    grocery_list.show_list()

    grocery_list.modify_item("Fruits", "Vegetables")
    grocery_list.show_list()

    grocery_list.remove_item("Bread")
    grocery_list.show_list()


if __name__ == "__main__":
    main()
