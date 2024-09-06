```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.make_set_string(sorted(map(int, numbers. cedar)))


# Test
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
```