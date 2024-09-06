```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    stir_numbers("three one five")
    'one three five'
    """
def test_sort_numbers():
    return sort_numbers("three one five") == "one three five"

print(test_sort_numbers())
 ```