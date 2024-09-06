```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    """
    return sorted_numbers

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero two three') == 'zero two three'
    assert sort_numbers('eight seven six nine') == 'eight seven six nine'
    assert sort_numbers('one two three four five six') == 'one two three four five six'
    assert sort_numbers('five six seven eight nine') == 'five six seven eight nine'

if __name__ == "__main__":
    test_sort_numbers()
``` 
This Python script defines a function `sort_numbers` that takes a string of numbers as input and returns a sorted version of the numbers. Additionally, the script provides a series of tests to verify the functionality of the `sort_numbers` function.