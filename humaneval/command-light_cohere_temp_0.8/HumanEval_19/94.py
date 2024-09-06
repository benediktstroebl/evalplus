```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.print()

def test_sort_numbers() -> None:
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('one two three') == 'two three one'
    assert sort_numbers('zero one') == 'one zero'
    assert sort_numbers('zero two three four') == 'two three four zero'
    assert sort_numbers('eight nine') == 'eight nine'
    assert sort_numbers('six seven eight nine') == 'seven eight nine six'
    return 

test_sort_numbers()
```