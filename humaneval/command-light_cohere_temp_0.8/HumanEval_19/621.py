```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
   wstr full numbers in sorted order, separated by spaces
    """
    numbers = numbers.split()
   n split()
    convert each integer into a string
    numbers.join() and sort them numbers from smallest to largest
    return " ".join(numbers)
    if __name__ == "__main__":
        unittest.TestCase().importTest

    assert sort_numbers('three one five') == 'one three five'
        unittest.TestCase.TestCase.TestCase(sort_numbers('two three six seven eight nine'))
        unittest.TestCase.TestCase.TestCase(sort_numbers('zero one three four five six seven eight nine'))
```  This code defines a function **`sort_numbers`** which sorts a given string of numbers from smallest to largest using the split and join method. The test cases ensure that the function is correctly implementing the sorting functionality.