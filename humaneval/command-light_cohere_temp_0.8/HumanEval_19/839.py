```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(n) for n in numbers.
    return ' '.join(sorted(numbers))
    """
    pass

    test_str = "three one five"
    expected = "one three five"
    assert sort_numbers(test_str) == expected
    return " succeeds"
```