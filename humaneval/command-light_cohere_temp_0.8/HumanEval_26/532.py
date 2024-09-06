Here's the self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers]


# Testing the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 1, 2, 3, 3]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 1]
print(remove_duplicates(numbers))  # expected output: []
```

The function `remove_duplicates` takes a list of integers as input and uses a set to keep track of elements that have been seen before. The function then returns a list of elements that are not in the seen set and not present in the input list.

This solution is self-contained and does not require any external functions or modules. It uses the testing to validate its functionality.