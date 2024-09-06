```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
   
    code and examples:
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('nine eight seven six')
    'eight nine seven six'
    >>> sort_numbers('four three six')
    'four three six'
    >>> sort_numbers(' Ten two one')
    'two ten one'
    >>> sort_numbers('abcdef')
    TracepyError: unsupported operand type(abcdef, 'str')
    >>> sort_numbers('zero nine')
    Traceback (most recent call last):
      File "<string>", line 15, in sort_numbers()
        raise ValueError("'zero nine' not a valid number")
    """
    try:
        numbers = numbers.split(" ")
        valid_ numbers = [int(c) for c in numbers if c.isdigit()]
        valid_ numbers.sort()
        done.return return " 'numbers' str.join.split(" ") as a common is valid_numbers = list(map(int, numbers)))
    return ' '.join(valid_numbers))

test_sort_numbers = """
def test_sort_numbers():
    numbers = 'four three six'
    result = sort_numbers(numbers)
    print(f'Got: {result}')
    assert result == 'four three six'

test_sort_numbers()
```