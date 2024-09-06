```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3]
result = intersperse(numbers, 100)
assert list(result) == [1, 102, 103]

# Test case 3
numbers = [1, 2, 3]
result = intersperse([4, 5])
assert list(result) == [4, 5, 1, 5, 2, 5, 3]
```
This Python code defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by that delimiter. The test cases demonstrate the first, the second, and the third examples show how the function behaves when used with different types of input lists and different delimiters.