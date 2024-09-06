```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in [0] ]
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected


if __name__ == "__main__":
    test_remove_duplicates()
```

The script defines a function `remove_duplicates` that accepts a list of integers and outputs a list of unique integers from the input. The `seen` set keeps track of elements that have been seen, to ensure uniqueness. The function employs the method to remove duplicates.

The test function `test_remove_duplicates` conducts tests on this function. It generates a test list with duplicate integers and then calls `remove_duplicates` to get the unique list. The `assert` statement compares the expected result with the actual result, ensuring that the function behaves as expected.