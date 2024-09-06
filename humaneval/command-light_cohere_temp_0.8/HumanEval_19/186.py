```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.
# tests
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero one two three four five six seven eight nine") == "zero eight seven six five four three two one"
    assert sort_numbers("10-1") == "10-1"
    assert sort_numbers(".") == ""
    assert sort_numbers("10 nine") == "10 nine"
    assert sort_numbers("one two three 4 five 6 seven eight 9") == "one seven nine 8 six 5 4 3 2 1"
```