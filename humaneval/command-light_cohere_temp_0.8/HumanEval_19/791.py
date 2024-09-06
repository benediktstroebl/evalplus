```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Numbers are sorted from smallest to largest.
    Return the process as a string with numbers in sorted order.

>>> numbers = 'three one five'
>>> sort_numbers(numbers)
'one threefive'

isort_numbers passes test cases. You can add more test cases to further test the function. 

**Note**: Replace the test string `numbers` with your test data.