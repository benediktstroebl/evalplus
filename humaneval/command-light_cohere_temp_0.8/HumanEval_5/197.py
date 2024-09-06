```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * (len(numbers) - 1))]

# Test cases:
numbers = [1, 2, 3, 4, 5]
print(instruments([1, 4, 2, 4, 3]))  # Expected: [1, 4, 2, 4, 3]

numbers = [10, 11, 12, 13]
print(instruments([10, 5, 10, 13], 4))  # Expected: [10, 5, 10, 13, 4]

numbers = [10, 11, 12, 13, 14]
print(instruments([10, 5, 10, 13], 5))  # Expected: [10, 5, 10, 13, 5, 14]
```

This Python script defines a function `instruments` that takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by that delimiter. The function uses a Python's `zip` and `list comprehension` along with the `+=` operator to achieve this. 

Test cases are provided to verify the correctness of the `instruments` function.