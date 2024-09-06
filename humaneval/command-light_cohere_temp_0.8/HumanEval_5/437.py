```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * (len(numbers) - 1))]

# Test cases
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

numbers = [10, 20, 30]
result = intersperse(numbers, 4)
assert list(result) == [10, 16, 20, 24, 30]

numbers = [10, 20, 30, 40]
result = intersperse(numbers, 4)
assert list(result) == [10, 16, 20, 24, 30, 40]

numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 5)
assert list(result) == [1, 5, 2, 5, 3, 6]

numbers = [10, 20, 30, 40, 50]
result = intersperse(numbers, 3)
assert list(result) == [10, 13, 16, 20, 24, 30, 40, 45]
```
This Python code defines a function `intersperse` that separates elements of a list with a specified delimiter. It creates test test cases to demonstrate the correctness of the function. The output of each test cases is then verified against the expected results.