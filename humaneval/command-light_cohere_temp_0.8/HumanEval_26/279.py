```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen]]


# Example test suite:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
``` 
This code implements a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The function uses a set to keep track of integers that have been encountered before, and then returns a new list containing only the integers that are not in the set. This is the way to avoid duplicates from a list.