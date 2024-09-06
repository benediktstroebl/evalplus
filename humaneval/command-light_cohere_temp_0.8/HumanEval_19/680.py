```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are specified by:
    - lower case 
    - numbers zero to nine
    """
    assert 'zero' in numbers.
    assert 'nine' in numbers
    assert 'one' in numbers.
    assert 'two' not in numbers
    assert 'three' in numbers
    assert 'four' not in numbers
    assert 'five' in numbers
    assert 'six' not in numbers
    assert 'seven' in numbers
    assert 'eight' in numbers
    assert 'six' in numbers 

    return numbers.sort_numbers(' three one five')
```