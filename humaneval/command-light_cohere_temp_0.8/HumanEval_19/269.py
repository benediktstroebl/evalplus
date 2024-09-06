```python
from typing import List
def sort_numbers(input_string: str) -> str:
    return input_string.

# Tests
def test_sort_numbers() -> None:
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero one two three four five six seven eight nine") == "zero eight nine"
    assert sort_numbers(" Ten twenty thirty forty fifty") == "ten forty fifty"
    assert sort_numbers("(one) (two) three four five six seven eight nine") == "(one two) three four five six seven eight nine"
    return
test_sort_numbers()
```