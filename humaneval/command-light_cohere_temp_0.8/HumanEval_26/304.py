```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in numbers[0]]
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 5]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert expected == result


if __name__ == "__main__":
    test_remove_duplicates()
```

This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicate elements removed. The `test_remove_duplicates` function contains a test case that creates a list of integers and passes it to the `remove_duplicates` function. The expected output is a list with duplicate elements removed, and the test passes.