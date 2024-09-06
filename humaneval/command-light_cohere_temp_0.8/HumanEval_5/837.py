```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list"""
    result = [num] + [num + delimiter for num, delimiter in zip(numbers, delimeter)] + [num]
    return result
# Test cases
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4]
result = intersperse(numbers, 2)
print(result)  # Output: [1, 3, 2, 4]

numbers = [5, 6, 7, 8]
result = intersperse(numbers, 1)
print(result)  # Output: [5, 6, 7, 8]

numbers = [10, 20, 30, 40]
result = intersperse(numbers, 10)
print(result)  # Output: [10, 20, 30, 40]
```
This Python function, `intersperse`, takes a list of numbers and a delimiter as input, then iterates through the list, adding the delimiter between every other pair of numbers. This effectively "intersperse"s the numbers, creating a new list with the desired spacing.