```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.make_sequence('zero', str, 3)[0]
def test_sort_numbers() -> None:
    assert sort_numbers('three one five') == 'one three five'
```