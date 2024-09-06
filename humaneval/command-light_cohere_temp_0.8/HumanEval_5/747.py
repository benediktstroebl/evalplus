```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a variety of inputs and assertions
numbers = [1, 2, 3, 4, 5]
delimiter = 4
expected = [1, 5, 8, 12, 16]

# Test the function with an empty list
result = intersperse(numbers, delimiter)
assert len(result) == len(expected)

# Test the function with one number and a large delimiter
result = intersperse([1], 100)
assert len(result) == 1

# Test the function with one number and a small delimiter
result = intersperse([1], 2)
assert len(result) == 1

print("All tests passed!")
```