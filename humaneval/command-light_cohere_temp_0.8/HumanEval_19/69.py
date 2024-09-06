Here is a Python script that includes a self-contained function that solves the problem of sorting numbers in markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 
    'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """

    # Separate numbers into a list
    numbers = [int(num) for num in numbers.
    # Sort the  numbers from smallest to largest
    sorted_numbers = sorted(numbers)
    return ' '.join(sorted_numbers)

# Unit tests
def test_sort_numbers():
    test_data = "three one five"
    expected = "one three five"
    result = sort_numbers(test_data)
    assert result == expected

# Run the tests
test_sort_numbers()
```

This script defines a function called sort_numbers, which takes a string of numbers as input and returns a sorted version of that string. The function splits the numbers into a list, sorts it, and then joins the sorted numbers back into a string.