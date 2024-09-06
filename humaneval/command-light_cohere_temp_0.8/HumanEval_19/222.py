Here is a self-contained Python script that defines and demonstrates the function `sort_numbers`:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()

  test_sort_numbers = """
    Input: three one five
    Expected Output: one three five
    """
    assert sort_numbers(test_sort_numbers) == "one three five"
``` 
The provided test string is used as an argument to the `assert` statement, which checks if the function's return value matches the expected output for the given input.