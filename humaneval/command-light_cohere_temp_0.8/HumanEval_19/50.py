```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.

def test_sort_numbers() -> None:
    """
    Test suite for the sort_numbers function
    """
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero two three four five six seven eight nine") == "zero eight seven six five four three two"
    assert sort_numbers("10") == "ten"
    assert sort_numbers("20210") == "2110"
    assert sort_numbers("asdfjsoughasdf") == "arfhgasdft"
    assert sort_numbers("hello world") == "world hello"
```