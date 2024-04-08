class Node():
    def __init__(self, data, next=None) -> None:
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-2]

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    @property
    def peek(self):
        if self.isEmpty():
            raise ValueError("empty stack")
        return self.head.next.data

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise ValueError("empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

s = Stack()
print("Length:", len(s))
print("Empty:", s.isEmpty())
print("Push 1-10")
for i in range(10):
    s.push(i + 1)
print("Peeking:", s.peek)
print("Items (bottom to top):", s)
print("Length:", len(s))
print("Empty:", s.isEmpty())

