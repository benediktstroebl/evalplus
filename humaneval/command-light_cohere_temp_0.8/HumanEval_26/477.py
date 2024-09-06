Here is a self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.is_duplicates]]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 5]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]  # True
    return result == [1, 2, 3, 4]  # False

# Run the function and test it
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
print(test_remove_duplicates())  # Output: False
```

This code provides a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements. The second test function `test_remove_duplicates` that checks if the result of calling `remove_duplicates` is the expected output for a given list of integers.