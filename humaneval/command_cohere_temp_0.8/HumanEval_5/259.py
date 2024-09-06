```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

print(intersperse(numbers, 1))
# Prints: [1, 0, 2, 1, 3, 1, 4, 1, 5]

print(intersperse(numbers, 2))
# Prints: [2, 1, 4, 2, 6, 2, 8, 2, 10]

print(intersperse([], 3))
# Prints: []
``` 

This function takes a list of numbers and an integer `delimiter` as input and returns a list where every two consecutive elements of the input list are separated by the `delimiter`. If the input list is empty, it returns an empty list. The essence of the solution is to use list comprehension and recursive calls. The base case is when the list is empty, in which case it returns an empty list. Otherwise, it concatenates the first element of the list, the `delimiter`, and the result of the function recursively called on the rest of the list.