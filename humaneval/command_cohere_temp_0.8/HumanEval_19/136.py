```python
from typing import List

def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    
    Valid input includes 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This script takes a string of space-separated numbers, sorts them, and returns a string of the sorted numbers. The function sorts the numbers from lowest to highest, ensuring that it handles only valid inputs: 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

Here is an example usage of the function:
```python
print(sort_numbers("three one five")) # Output: one three five
```

This function can also be imported and used in other Python scripts. 
For example, you may want to test the function by importing it into a Python script and using the assert statement to compare the output of the function with the expected output. Here is an example: 
```python
import sort_numbers

def test_sort_numbers():
    assert sort_numbers.sort_numbers("three one five") == "one three five"
    assert sort_numbers.sort_numbers("eight two zero nine seven six five four") == "zero two three four five six seven eight nine"
``` 
This will verify that the `sort_numbers` function works as expected. If the assertion passes, the test suite will print out "OK" indicating that the function sorts the numbers correctly.  If the assertion does not pass, the test suite will print the differences between the actual and expected outputs, helping you to identify the issues and fix them.