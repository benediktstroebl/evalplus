```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.
    return ''.join(sorted(numbers, reverse=True))
#Tests
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
```