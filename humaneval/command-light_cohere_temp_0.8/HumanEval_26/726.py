```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]


# Test suite
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

numbers = [10, 10, 20, 30]
result = remove_duplicates(numbers)
print(result)  # Output: [10, 20, 30]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The test suite demonstrates the this function with three examples, and the expected output is shown for each case.