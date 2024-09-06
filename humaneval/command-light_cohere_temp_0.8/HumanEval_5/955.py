```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[1:]

# Test the function with various inputs and check the output using built-in assert
numbers = [1, 2, 3, 4]
assert list(intersperse(numbers, 2)) == [1, 2, 4, 3, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
assert list(intersperse(numbers, 3)) == [1, 2, 3, 4, 5, 3]

numbers = [10, 20, 30, 40]
assert list(intersperse(numbers, 10)) == [10, 20, 30, 40, 10, 20, 30, 40]
```