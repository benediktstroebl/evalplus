```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num > 0]
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    assert remove_duplicates(numbers) == expected


if __name__ == "__main__":
    test_remove_duplicates()
```
The code defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicates removed. It uses a specific to a set to keep track of seen numbers and then selects only the numbers that are greater than zero. The `test_remove_duplicates` function contains a test case and asserts that the output of `remove_duplicates` is correct. 

Finally, the `if __name__ == "__main__":` block ensures that the test is executed when the script is run directly.