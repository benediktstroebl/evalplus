```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and x not in numbers[0]]
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    assert remove_duplicates(numbers) == expected


if __name__ == "__main__":
    test_remove_duplicates()
```
This code defines a function **`remove_duplicates`** that takes a list of integers as input and returns a new list with duplicate elements removed. It uses a also a set to keep track of seen elements and creates a new list with all elements that are not duplicates. The **`test_remove_duplicates`** function tests this function with a sample list and asserts that the result is as expected.