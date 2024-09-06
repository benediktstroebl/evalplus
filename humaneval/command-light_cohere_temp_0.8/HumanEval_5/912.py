```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 2) + numbers

# Test cases
numbers = [1, 2, 3, 4, 5]
print(invisalign([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]

numbers = [6, 7, 8, 9]
print(invisalign([6, 7], 4))  # Expected: [6, 4, 7, 8, 9]

numbers = [10, 2, 3, 4, 5]
print(invisalign([10], 4))  # Expected: [10, 4, 10, 5]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(invisalign([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]
```

The `invisalign` function takes a list of numbers and a delimiter as input. It uses list comprehension and slicing, and the `+` operator to achieve the desired result.