```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+j for i,j in zip(numbers, numbers[1:]+[delimeter])]

# Test case 1: empty list
numbers = []
print(inperseperate(numbers, 4))  # Expected: []

# Test case 2: list with 2 consecutive numbers
numbers = [1, 2]
print(inperseperate(numbers, 4))  # Expected: [1, 6]

# Test case 3: list with 3 consecutive numbers
numbers = [1, 2, 3]
print(inperseperate(numbers, 4))  # Expected: [1, 4, 2, 4, 3]

# Test case 4: list with 4 consecutive numbers
numbers = [1, 2, 3, 4]
print(inperseperate(numbers, 4))  # Expected: [1, 4, 2, 4, 3]

# Test case 5: list with 5 consecutive numbers
numbers = [1, 2, 3, 4, 5]
print(inperseerate(numbers, 4))  # Expected: [1, 4, 2, 4, 6]
```

The provided Python script defines a function `inperseperate` that separates lists into consecutive elements with a specified `delimiter`. The test cases validate the function's output for various input lists.