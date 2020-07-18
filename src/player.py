# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
