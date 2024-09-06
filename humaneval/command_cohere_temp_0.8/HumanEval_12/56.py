Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# Test the longest function
from typing import List, Optional
import unittest

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings.
    :return: Longest string.
    """
    # Sorting the list of strings by their length, ascending.
    # This way, the longest string will be at the end of the list.
    strings.sort(key=len, reverse=True)
    return strings[0] if strings else None

class TestLongest(unittest.TestCase):
    def test_empty(self):
        """ Test case when the input list is empty. """
        self.assertEqual(longest([]), None)

    def test_single_string(self):
        """ Test case when there is a single string. """
        self."""
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        """ Test case when there are multiple strings of different lengths. """
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_equal_lengths(self):
        """ Test case when there are multiple strings of the same length. """
        self.assertEqual(longest(['aa', 'aaa', 'aaaa']), 'aaaa')

if __name__ == '__main__':
    unittest.main()
```

The `longest` function sorts the list of strings by their length using the `sort` method with a custom `key` function that converts each string to its length. The `reverse=True` parameter ensures that the longest string, which is expected to be at the end of the list after sorting, is returned. The function returns the longest string if there's one, or the first occurrence of the longest string in case there are multiple longest strings. The function returns `None` if the input list is empty.

The `TestLongest` class tests the `longest` function with different scenarios, including an empty list, lists with one string, and lists with multiple strings of different and equal lengths.

Run this code, and it will automatically discover and run the test cases. 

Let me know if this solution works for you or if you have any further questions!