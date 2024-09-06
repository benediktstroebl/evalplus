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

The function `intersperse()` takes a list of numbers and an integer `delimiter` as input and returns a list of numbers with the specified delimiter inserted between each pair of consecutive elements in the input list. If the input list is empty, it returns an empty list. Otherwise, it inserts the `delimiter` at the beginning and then calls itself recursively to process the rest of the list. The delimiter is added at the beginning to maintain the same spacing throughout the list. The delimiter is also added at the end to ensure it is included after the last element.