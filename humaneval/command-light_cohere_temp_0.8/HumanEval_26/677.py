```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


# Test the function
numbers = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

numbers = [4, 4, 2, 2, 3]
result = remove_duplicates(numbers)
print(result)  # Expected output: [2, 3]

numbers = [1, 2, 2, 3, 1, 3, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4]
```

This script provides a `remove_duplicates` function, which accepts a list of integers and outputs a new list with all distinct integers from the original list. It is tested this function by creating a new list and filtering out all duplicated numbers from the original list using the `count()` method.