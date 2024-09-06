```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()
 string. string least numbers.

    def test test_ a string in the given format,
    except numbers containing characters other than digits."""
    # Remove all non-digit characters
    numbers = numbers.replace(str.replace(' ', ''). for _ in numbers if '9'.isdigit())
    # Convert the string of numbers into a list
    num_list = list(numbers)
    # Sort the list of numbers
    sorted_numbers = sorted(num_list)
    # Convert the sorted list back into a string
    return ' '.join(sorted_numbers)

# Unit tests
test_sort_numbers = """
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
"""
# Run the unit tests
test_sort_numbers()
```