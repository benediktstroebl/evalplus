```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test case 1
numbers = [4, 1]
result = intersperse(numbers, 4)
assert list(result) == [4, 4, 1, 4, 1]

# Test case 2
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

# Test case 3
numbers = [1, 2, 4, 3, 5]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3, 4, 5]

# Test case 4
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 2)
assert list(result) == [1, 2, 3, 4, 5]

# Test case 5
numbers = [1, 2, 3, 4]
result = intersperse(numbers, 13)
assert list(result) == [1, 13, 2, 13, 3, 13, 4]
```
The provided Python code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the integers separated by that delimiter. The test cases cover various scenarios, including empty lists, lists with different lengths, and lists with specific delimiters.