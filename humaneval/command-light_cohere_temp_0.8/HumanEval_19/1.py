```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """Sorts numbers from smallest to largest and returns them as a string in the correct order.
    >>> sorted_numbers('three one five')
    'one three five'
    """
    input_list = List(map(int, input_str.split()))
    return ' '.join(sorted(input_list))

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'

# Example usage:
test_sort_numbers()
 ``` 
This code defines a function sort_numbers that takes a string of numbers separated by spaces as input and returns a string with the numbers sorted from smallest to largest. The function uses the test_numbers function to validate the output.