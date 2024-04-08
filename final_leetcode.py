from collections import deque
class FrontMiddleBackQueue:
    def __init__(self):
        self.deque = deque()

    def pushFront(self, val: int) -> None:
        self.deque.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        middle = len(self.deque) // 2
        self.deque.insert(middle, val)

    def pushBack(self, val: int) -> None:
        self.deque.append(val)

    def popFront(self) -> int:
        if not self.deque:
            return -1
        return self.deque.popleft()

    def popMiddle(self) -> int:
        if not self.deque:
            return -1
        middle_index = (len(self.deque) - 1) // 2
        for _ in range(middle_index):
            self.deque.append(self.deque.popleft())
        popped_middle = self.deque.popleft()
        for _ in range(middle_index):
            self.deque.appendleft(self.deque.pop())
        return popped_middle

    def popBack(self) -> int:
        if not self.deque:
            return -1
        return self.deque.pop()
