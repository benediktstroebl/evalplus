```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.make_sort_key_string(sorted(numbers.numsortstring())  # convert numbers to a string)

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
```