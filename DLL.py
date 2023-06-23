class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return

            current = current.next

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return current

            current = current.next

        return None

    def display(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.data)
            current = current.next

        print(elements)


dll = DoublyLinkedList()

dll.append("1")
dll.append("2")
dll.append("3")
dll.display()

dll.delete("3")
dll.display()

result = dll.search("4")
if result:
    print("Node found:", result.data)
else:
    print("Node not found")
