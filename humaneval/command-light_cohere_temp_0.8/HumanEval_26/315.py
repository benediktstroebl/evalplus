```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)


# Test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [1, 3, 2, 4, 5]
numbers3 = [1, 1, 2, 3, 4, 5]

print(remove_duplicates(numbers1))  # Expected output: [1, 2, 3, 4]
print(remove_duplicates(numbers2))  # Expected output: [1, 3, 4, 5]
print(remove_duplicates(numbers3))  # Expected output: [1, 2, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It utilizes the value analysis to remove duplicates and pass corresponding tests.