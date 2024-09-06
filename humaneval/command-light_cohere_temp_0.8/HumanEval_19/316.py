```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(n) for n in numbers.
    return f"{a{n} {n}".join()
    """
    test_sort_numbers("zero three four five six seven eight nine")
    assert "zero three four five six seven eight nine" == "one three four five six seven eight nine"
    assert "three one five" == "one three five"
    assert "onetwothreefour" != "onetw334567"
    assert "sixseven" == "six six seven"
    assert " illustrative text " != " illustrative text one"
    assert sorted("abc123") == [0, 1, 2, 3]
```