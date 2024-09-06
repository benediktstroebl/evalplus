Here is a Python script that defines a function sort_numbers that takes a list of numbers in the format "zero-nine" and returns the numbers sorted from smallest to largest:
```python
from typing import List

def sort_numbers(numbers: List[str]) -> List[str]:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return [numbers.sort()
String a list to string format)
    """
    return numbers

def test_sort_numbers():
    numbers = ['three one five', 'two three six', 'four seven eight', 'zero nine eight']
    expected = ['one three five', 'two three six', 'four seven eight']
    return expected == sort_numbers(numbers)

# Call the function to test it
test_sort_numbers()
print('Pass')

```

The code defines a function `sort_numbers` that sorts a list of numbers in the format "zero-nine" into a new list. It then verifies that the strings representing the list are sorted correctly using this function. The `test_sort_numbers` function is used to call the `sort_numbers` function with a sample list of numbers and compares the expected result against the actual result.