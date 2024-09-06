```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the specified prefix. The function uses a list comprehension, creating and returning a new list by applying a conditional check to each element in the input list. 

To test this implementation, you can create a test script with the following content:
```python
import unittest

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list_no_prefix(self):
        """Empty list, no common prefix"""
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_empty_list_with_prefix(self):
        """Empty list, with common prefix"""
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_list_with_prefix(self):
        """List with values with and without common prefix"""
        self.$assertListEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_list_with_substring_prefix(self):
        """List with values with substring common prefix"""
        self.$assertListEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar'), ['array'])

if __name__ == '__main__':
    unittest.main()
```

The script is tested using `unittest` framework. The test cases are defined as methods starting with the prefix `test_`, and the `assert*` methods are used to check the test conditions. 

To run the tests, you can save the Python script in a file and execute it from the command line by typing `python filename.py`. 

The script should pass all four test cases.  If it does, it means the function is correctly filtering the list of strings based on the given prefix.