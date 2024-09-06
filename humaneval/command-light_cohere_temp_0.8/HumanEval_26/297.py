```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[:seen.][:seen.count(num)] == 1]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]


def test_remove_duplicates_recursive():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]


if __name__ == "__main__":
    test_remove_duplicates()
    test_remove_duplicates_recursive()
```
The above script provides two test functions `test_remove_duplicates` and `test_remove_duplicates_recursive` to check if the `remove_duplicates` function works correctly. 

The function `remove_duplicates` removes duplicate elements from a list of integers and returns a new list with unique integers.