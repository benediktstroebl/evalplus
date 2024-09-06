```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Tests
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
assert len(result) == 6

numbers = [5, 6, 7]
result = intersperse(numbers, 10)
assert len(result) == 7

numbers = [3, 4, 5]
result = intersperse(numbers, 100)
assert len(result) == 6
```
This Python script defines a function `intersperse` that takes two arguments: a list of numbers and a delimiter as an integer. The function uses list comprehension to append each number with the delimiter to the original list.