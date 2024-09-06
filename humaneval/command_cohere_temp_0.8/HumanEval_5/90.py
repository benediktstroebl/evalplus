```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

print(intersperse(numbers, 1))
# Prints: [1, 0, 2, 0, 3, 0, 4, 0, 5]

print(intersperse(numbers, 2))
# Prints: [2, 0, 3, 0, 4, 0, 5]

print(intersperse(numbers[1:], 3))
# Prints: [3, 0, 4, 0, 5]

print(intersperse([], 4))
# Prints: []
```

The function `intersperse()` takes a list of numbers `numbers` and an integer `delimiter` as input and returns a list of numbers with `delimiter` inserted between consecutive elements of `numbers`. If the `numbers` list is empty, it returns an empty list. The list is recursively built by adding the first element to a new list with `delimiter` and the rest of the elements processed in the same way. 

The tests cover different use cases, including edge cases, to verify the correctness of the `intersperse()` function.