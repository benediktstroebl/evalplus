```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]


# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [3, 2, 1, 3, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]

numbers = [1, 1, 2, 2]
print(remove_duplicates(numbers))  # Expected output: [1, 2]

numbers = [5, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # Expected output: [2, 3, 4, 5]

numbers = List(set([5, 2, 3, 4, 5]))
print(remove_duplicates(numbers))  # Expected output: [2, 3, 4, 5]
```

This code defines a `remove_duplicates` function that takes a list of integers as input and returns a new list with all distinct integers from the original. The function utilizes the using the set and list comprehension to achieve this. It removes duplicate elements from the simple and efficient way.