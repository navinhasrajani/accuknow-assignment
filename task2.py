class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # Internal state for iteration

    def __iter__(self):
        self._index = 0  # Reset index at the start of iteration
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # End of iteration

# Example Usage
rect = Rectangle(10, 5)

# Iterating over the instance
for dimension in rect:
    print(dimension)
