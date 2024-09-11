```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring to search for.

    Returns:
    List[str]: The filtered list of strings.
    """
    # Use list comprehension to filter strings that contain the substring
    return [string for string in strings if substring in string]

# Test cases
import unittest

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_strings_with_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_no_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'x'), [])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `filter_by_substring` function and includes test cases using the `unittest` module. The function uses list comprehension to filter strings that contain the given substring. The test cases cover the scenarios where the input list is empty, contains strings with the substring, and contains strings without the substring.