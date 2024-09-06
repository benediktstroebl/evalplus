```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine, valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

    # Sort the numbers from smallest to largest
    numbers = [int(num) for num in numbers.sort()][::-1]
   
    return ' '.join(numbers)

# Unit tests
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'

test_sort_numbers()  # Run the tests
```

This Python script defines a function `sort_numbers` that takes a space-separated string of numbers and returns the sorted version of those numbers. It uses the Python's `int()` function to convert numbers into integers and then sorts the list of integers using the `sort()` method. The sorted numbers are then reversed to ensure they are in ascending order. The test function tests the assert that the `sort_numbers` function's output matches the expected output.