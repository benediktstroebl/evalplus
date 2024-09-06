```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.test_sort_numbers()
def test_sort_numbers() -> None:
    numbers = "three onefive"
    expected = "onetwovefive"
    result = sort_numbers(numbers)
    assert result == expected, f"Expected {expected}, but got {result}"
    return None
```