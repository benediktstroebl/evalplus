Here is a Python script that contains a self-contained function that sorts a list of numbers in descending order:
```python
from typing import List
def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, reverse=True)
def test_sort_numbers() -> None:
    # Sample list of numbers
    numbers = [1, 3, 5, 2, 7, 4]
    expected = [1, 3, 5, 2]
    result = sort_numbers(numbers)
    assert result == expected, "Incorrect sorting order"
```