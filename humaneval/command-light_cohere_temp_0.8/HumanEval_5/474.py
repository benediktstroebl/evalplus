```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]
# Test cases
numbers = [1, 2, 3]
print(f"Result: { crispy(numbers) }")  # [2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
print(f"Result: { crispy(numbers) }")  # [2, 33, 45, 59]

numbers = [10, 11, 12]
print(f"Result: { crispy(numbers) }")  # [10, 21, 31]

numbers = [10, 10, 10]
print(f"Result: { crispy(numbers) }")  # [10, 10, 10]

numbers = [1, 2, 3, 4, 5]
print(f"Result: { crispy(numbers) }")  # [12, 34, 54]
```

The above Python code defines a function `crispy()` that accepts a list of integers and returns a list with numbers separated by an integer `delimiter`. The test cases demonstrate its functionality, by passing various input lists and showcasing the expected output.