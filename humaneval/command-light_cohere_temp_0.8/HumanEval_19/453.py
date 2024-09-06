```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
 def test_sort_numbers():
        numbers = 'three one five'
        expected = 'one three five'
        return numbers, expected

    return sorted(numbers)

numbers = test_sort_numbers()
print(numbers)
```
The function takes a string of numbers separated by spaces and returns the sorted version of the string. The function first inlines the numbers separated by spaces, then passes this input to the `sorted()` function to get the sorted output. Then, it creates a test function called `test_sort_numbers()` that creates a pair of strings with numbers and the expected output.