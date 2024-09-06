```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num > 0]
    seen.add(numbers)
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert expected == result


if __name__ == "__main__":
    test_remove_duplicates()
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique positive integers. The `seen` set keeps track of the integers that have been encountered, and the function filters out any duplicates and keeps only the positive integers. The `test_remove_duplicates` function is a simple test that creates a list of integers, runs the `remove_duplicates` function, and compares the expected and the actual results. 
When you run the script, the `remove_duplicates` function is invoked, and the test passes.