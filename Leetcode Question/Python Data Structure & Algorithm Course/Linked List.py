# Basic linked list structure
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}
# To access 23
# print(head["next"]["next"]["value"])



# only for creating a new node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked list constructor
class LinkedList:
    # create a new Node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(4)

print(my_linked_list.head.value)

    # # create a new node and add the node to end
    # def append(self, value):
    #
    # # create a new node and the node to beginning
    # def prepend(self, value):
    #
    # # create a new node and add the node to certain index
    # def insert(self, index, value):

