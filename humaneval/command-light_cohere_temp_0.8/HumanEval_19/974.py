Here is a self-contained Python script with a function that sorts a list of numbers in ascending order:
```python
from typing import List
def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers)
def test_sort_numbers() -> None:
    numbers = [1, 3, 5]
    expected = [1, 3, 5]
    actual = sort_numbers(numbers)
    assert expected == actual, f"Expected: {expected}, but got: {actual}"
```