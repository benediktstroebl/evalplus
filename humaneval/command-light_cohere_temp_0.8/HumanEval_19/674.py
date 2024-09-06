Here's a self-contained Python script that defines and executes the function sort_numbers to solve the problem you provided:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split().numbers.split(' ', sorted(numbers)).join(" ")
```
This function splits the input string into a list of numbers, sorts them in ascending order, and then joins the sorted numbers back into a string to return.

To execute the function and test it with various inputs, use the unittest module:
```python
import unittest

class unittest.TestCase(TestCase)(
    test_suite="sort_numbers_test",
    surfaces=[
        'sort_numbers',
    ])
```
The test suite will automatically find and run all the defined tests. 
The output will be the test results.