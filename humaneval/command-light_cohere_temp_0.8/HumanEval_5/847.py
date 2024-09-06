```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter]

# Test cases
numbers = [1, 2, 3, 4, 5]
delimiter = 4
expected = [1, 4, 2, 4, 3, 4, 5]
print(f'Test 1: {expected}', end=' ')
print(f'vs actual: {inperse(numbers, delimiter)}')

numbers = [0, 2, 4, 6]
delimiter = 4
expected = [0, 4, 2, 6]
print(f'Test 2: {expected}', end=' ')
print(f'vs actual: {inperse(numbers, delimiter)})
```

This code defines a function `inperse` that takes a list of integers `numbers` and a delimiter integer `delimiter` as inputs, and returns a new list that adds a copy of the delimiter at the beginning of every pair of consecutive elements. The code then uses this test cases to verify the correctness of the `inperse` function.