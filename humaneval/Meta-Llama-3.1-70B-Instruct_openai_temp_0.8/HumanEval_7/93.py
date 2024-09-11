```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to filter
    substring (str): A substring to filter by

    Returns:
    List[str]: A list of strings containing the given substring
    """
    # Use list comprehension to filter the input list
    # The if condition checks if the substring is present in each string
    return [string for string in strings if substring in string]


# Example use cases:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']

# Test cases to verify the functionality
import unittest

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_list_with_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_list_without_matches(self):
        self.assertEqual(filter_by_substring(['bcd', 'cde', 'def'], 'a'), [])

if __name__ == '__main__':
    unittest.main()
```