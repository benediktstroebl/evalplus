```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.

def test_sort_numbers() -> None:
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero four five six three") == "four five six three"
    assert sort_numbers("Eight Nine") == "Nine Eight"
    assert sort_numbers(" Tenn13") == "Ten Thirteen"
    assert sort_numbers("10 IV") == "One Zero Four"
    assert sort_numbers("abc123") == "123 abc"
    assert sort_numbers("") == ""
```