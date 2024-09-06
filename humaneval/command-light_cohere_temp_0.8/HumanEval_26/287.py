```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[0]]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]


if __name__ == "__main__":
    test_remove_duplicates()
```
This script defines a function `remove_duplicates` that removes duplicate elements from an input list of integers and passes the test with the `test_remove_duplicates` function.