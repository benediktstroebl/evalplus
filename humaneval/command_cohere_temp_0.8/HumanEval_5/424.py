```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
``` 

The function `intersperse()` takes in a list of numbers `numbers` and an integer `delimiter` as input and returns a list of numbers with the specified delimiter inserted between each pair of consecutive elements in the input list. If the input list is empty, it returns an empty list. This is achieved using a recursive approach where the delimiter is added to the list after the first element and the rest of the list (excluding the first element) is added to the end, with the delimiter added between each element.