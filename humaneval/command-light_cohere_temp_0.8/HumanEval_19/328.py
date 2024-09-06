```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
 def test_sort_numbers() -> None:
        numbers = "three one five"
        expected = "one three five"
        actual = sort_numbers(numbers)
        assert actual == expected

        numbers = "nine eight seven six five four three two one"
        expected = "four three two one seven six five eight nine"
        actual = sort_numbers(numbers)
        assert actual == expected

    return sorted

# Call the function with test inputs and check the results against expected outputs.
test_sort_numbers()
```