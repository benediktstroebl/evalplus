```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.list(map(int, numbers. Roman digits, from '0' to '9')

def test_sort_numbers() -> None:
    inputs = """
    three one five
    five three
    nine eight seven six
    """
    expected = """
    one three five
    five nine eight seven
    """
    assert sort_numbers(inputs) == expected, "Error in sorting numbers"
```