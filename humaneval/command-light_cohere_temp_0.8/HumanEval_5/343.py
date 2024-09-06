```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[1:] 

# Test cases
numbers = [1, 2, 3, 4, 5]
delimiter = 4

expected = [1, 4, 2, 4, 3, 5]
result = intersperse(numbers, delimiter)
assert list(map(int, expected)) == list(map(int, result))

# Another test
numbers = [10, 20, 30]
delimiter = 13
expected = [10, 13, 20, 30]
result = intersperse(numbers, delimiter)
assert list(map(int, expected)) == list(map(int, result))
```
This code defines a Python function `intersperse` that takes a list of integers and an integer `delimiter` as parameters. The function returns a `numbers + [delimiter] + numbers[1:]`, which inserts the `delimiter` integer between every two consecutive elements in the input list.