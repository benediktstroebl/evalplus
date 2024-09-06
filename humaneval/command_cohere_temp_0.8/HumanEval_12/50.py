Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# Script for solving the longest string problem
from typing import List, Optional
import unittest

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings.
    :return: Longest string or None.
    """
    # Check for empty list
    if not strings:
        return None
    
    # Use a variable to track the maximum length and the corresponding element.
    longest_len = 0
    longest_str = None
    
    # Iterate through the list and update the variables as needed.
    for str_ in strings:
        if len(str_) > longest_len:
            longest_len = len(str_)
            longest_str = str_
    
    return longest_str

# Unit tests
class TestLongest(unittest.TestCase):
    def test_longest_with_empty_list(self):
        self.assertIsNone(longest([]))
    
    def test_longest_with_single_string(self):
        self.assertEqual(longest(['a']), 'a')
    
    def test_longest_with_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()
```
This code includes a `longest` function to find the longest string among a list of strings, along with unit tests to validate its behavior. 

The function uses a loop to iterate through the input list of strings, tracking the longest string so far. It returns the longest string if there's only one of the same length, or the first occurrence of the longest string. If the input list is empty, the function returns `None`.

The unit tests check the function's behavior across various scenarios, ensuring it matches the expected output for empty lists, single strings, and multiple strings. 

When you run the script, the `unittest` module automatically executes the test cases and reports on whether the function's behavior matches the expected output.