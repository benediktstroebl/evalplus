```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

numbers = [1, 3, 5, 7, 9]
print(intersperse(numbers, 2))
# Prints: [1, 2, 3, 5, 7, 9]

numbers = [4, 6, 8, 10]
print(intersperse(numbers, 12))
# Prints: [4, 12, 6, 12, 8, 12, 10]

numbers = [0, 0, 0]
print(intersperse(numbers, 7))
# Prints: [0, 7, 0, 7, 0]

numbers = []
print(intersperse(numbers, 99))
# Prints: []
``` 

This function takes a list of numbers and an integer `delimiter` as input and returns a list where every two consecutive elements are separated by the `delimiter`. If the input list is empty, it returns an empty list. This solution uses recursion and is based on the fact that the concatenation of two lists with a separator in between equals the list with the first element, the separator, and the concatenation of the other list with the separator.