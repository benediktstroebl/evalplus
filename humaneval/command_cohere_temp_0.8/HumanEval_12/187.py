Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# Test the longest function
from typing import List, Optional
import unittest

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    :param strings: List of strings.
    :return: Longest string or None.
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the result
    longest_str = strings[0]
    
    # Check for other strings of the same length and update if needed
    for strng in strings:
        if len(strng) > len(longest_str):
            longest_str = strng
    
    return longest_str

class TestLongest(unittest.TestCase):
    def test_empty_input(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_strings_same_length(self):
        self.assertEqual(longest(['Hello', 'World', '!']), 'Hello')

if __name__ == '__main__':
    unittest.main()
```

The `longest` function is designed to accept a list of strings, prioritize the longest one, and return the first string among equal candidates. This is achieved through a loop that compares the lengths of all strings in the input list, updating the `longest_str` variable as necessary. The function also handles an empty input list by returning `None`, making it robust against edge cases.

The test suite, facilitated by `unittest`, comprises multiple test cases to validate the behavior of the `longest` function. Specifically, `test_empty_input` checks that the function returns `None` when the input list is empty. `test_single_string` and `test_multiple_strings` ensure that the function correctly identifies the longest string in cases of single and multiple strings, respectively. Finally, `test_multiple_strings_same_length` verifies that the function correctly picks the first string among those of equal length.

Running the script using `python test.py` will execute the test suite, providing clear assertions that the `longest` function operates as expected. Adjustments to the code or additions of more test cases can easily be made for increased reliability.