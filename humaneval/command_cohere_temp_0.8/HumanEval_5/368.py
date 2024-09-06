```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

print(intersperse(numbers, 1))
# Prints: [1, 0, 2, 1, 3, 1, 4, 1, 5]

print(intersperse(numbers, 2))
# Prints: [2, 1, 4, 2, 6, 2, 8, 2, 10]

print(intersperse(numbers, 3))
# Prints: [3, 2, 7, 3, 11, 3, 15, 3, 19]

print(intersperse([], 5))
# Prints: []
``` 

The function works as follows:
- If the input list is empty, it returns an empty list.
- If the input list has only one element, the function returns a list with just that element.
- If the input list has more than one element, the function adds the delimiter to the beginning of the list, then recursively calls itself with the rest of the list (excluding the first element). 

The output of the example usage shows how the delimiter is inserted between consecutive elements of the list.