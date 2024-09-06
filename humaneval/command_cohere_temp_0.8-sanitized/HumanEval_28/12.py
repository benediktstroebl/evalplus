from typing import List, Generic, TypeVar
T = TypeVar('T')
class SingletonList(Generic[T]):
    """A list that can contain only one element."""

    def __init__(self, value: T):
        """Initializes the list with a value."""
        self._value = value
        self.l = []

    def add(self, value: T) -> bool:
        """Adds a value to the list if it is not already present."""
        if value not in self.l:
            self.l.append(value)
            return True
        return False

    def get_value(self) -> T:
        """Returns the value of the list, or None if the list is empty."""
        return self._value if self.l else None

    def __len__(self) -> int:
        """Returns the number of items in the list."""
        return len(self.l)

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        return str(self.l)
def concatenate(strings: SingletonList[str]) -> str:
    """Concats the strings in the list separated by space"""
    return " ".join(strings)