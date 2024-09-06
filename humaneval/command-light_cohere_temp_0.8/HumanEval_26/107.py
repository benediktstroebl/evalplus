```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen]]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 5, 3, 4, 6]
    expected = [1, 3, 4, 5, 6]
    actual = remove_duplicates(numbers)
    assert expected == actual


if __name__ == "__main__":
    test_remove_duplicates()
```
The function `remove_duplicates` takes a list of integers as input and returns a new list with duplicates removed. The `set` object is used to keep track of the elements that have already been seen, ensuring that only elements not in the set are added to the result list.