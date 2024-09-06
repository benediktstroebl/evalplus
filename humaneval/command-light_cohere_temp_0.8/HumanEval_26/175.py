```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


# Test cases
numbers = [1, 2, 3, 2, 4, 2, 3, 1]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]

numbers = [3, 2, 4, 2, 3, 5]
print(remove_duplicates(numbers))  # Expected output: [3, 4, 5]

numbers = [1, 2, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 1, 4, 3]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The test cases demonstrate the expected outputs.