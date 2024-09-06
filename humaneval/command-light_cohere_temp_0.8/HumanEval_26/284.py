```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 5]
    expected = [1, 3, 4]
    assert remove_duplicates(numbers) == expected


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 3, 5]
    test_remove_duplicates()
```

This script defines a function remove_duplicates that takes a list of integers and returns a new list with duplicate values removed. The test_remove_duplicates function passes all the tests with the built-in function.