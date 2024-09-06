```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
    return result


numbers = [1, 2, 3, 2, 4, 3, 1]
print(test_remove_duplicates())  # Expected: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers from the original. It also includes a test function to verify the correctness of the `remove_duplicates` function.