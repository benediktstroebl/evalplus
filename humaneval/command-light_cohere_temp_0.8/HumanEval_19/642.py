```python
import stringIO
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers.
    return ' '.join(sorted(numbers))
    """

def test_sort_numbers():
    input_str = "three one five"
    expected_str = "one three five"
    result = sort_numbers(input_str)
    assert result == expected_str, f"Expected '{expected_str}', but got '{result}'"

# Run the function and test it out
input_file = stringIO.StringIO('three string to be sorted:\n' + 'three one five\n')
test_sort_numbers()  # Will raise an AssertionError if the function doesn't solve correctly

The output should be: one three five