```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num > 0]
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 3, 5]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected


if __name__ == "__main__":
    test_remove_duplicates()
```

The provided code defines a `remove_duplicates` function that removes duplicate positive integers from the input list. The function uses a set to keep track of numbers seen so far, and then iterates through the input list, removing any numbers that are not in the set or are zero. The `test_remove_duplicates` function contains a simple test that uses the `remove_duplicates` function with a sample input list and checks that the resulting list contains the expected elements.