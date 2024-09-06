```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * (len(numbers) - 1))]

# Test case:
numbers = [1, 2, 3, 4]
result = intersperse(numbers, 4)
print(result)  # Expected Output: [1, 4, 2, 4, 3]
```
This Python script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list where numbers are separated every 2 consecutive elements with the provided delimiter. 

The `test_case` section demonstrates how the function works by passing a test list [1, 2, 3, 4] with a delimiter of 4 and printing the resulting list.