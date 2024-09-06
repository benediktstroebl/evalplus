```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ', numbers). specific to sort to intal digit from '0' to '9'
    >> sorted(numbers)
def test_sort_numbers(test_str: str) -> None:
    expected_sorted = 'one three five'
    actual_sorted = sort_numbers(test_str)
    if actual_sorted != expected_sorted:
        raise Exception('Sorted numbers do not match the expected output!')
test_sort_numbers('three one five')
```