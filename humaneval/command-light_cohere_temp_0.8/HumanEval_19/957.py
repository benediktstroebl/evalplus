```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    """

    def test_sort_numbers():
        string = "three one five"
        expected = "one three five"
        return expected == sort_numbers(string)

    if test_sort_numbers():
        print("Test passed.")
    else:
        print("Test failed.")
```
This Python code defines a function `sort_numbers` that sorts a given string of numbers in alphabetical order. The function takes a input as a string containing numbers, and returns a sorted version of the string. The function employs a `numbers` list comprehension to convert each number into an integer, then sorts the list and joins the sorted numbers back into a string. The code also includes a function `test_sort_numbers`, which is used to verify if the `sort_numbers` function's output matches an expected result. If the test passes, the code prints "Test passed"; otherwise, it prints "Test failed".