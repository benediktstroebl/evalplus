```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers. The list is sorted from smallest to largest (reverse) and converted back to string.
    return ' '.join(numbers)
    """
    test_sort_numbers = """
    five three 
    six four 
    zero one 
    three """
    assert sort_numbers(test_sort_numbers) == 'six four three zero one'.
```