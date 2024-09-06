```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. The function utilizes list comprehension, creating a new list by filtering strings using the `startswith` method. 

To showcase the function, we can create a test script. Firstly, the function is imported, and the first test is executed to confirm that the function returns an empty list when an empty list of strings is provided. Secondly, the second test ensures that the function returns a list containing only strings that start with the given prefix when provided a list of strings and a prefix. 

The following code provides a test script confirming the correct functionality of the `filter_by_prefix` function: 
```python
import unittest
from filtering import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_by_prefix(self):
        strings = ['abc', 'bcd', 'cde', 'array']
        prefix = 'a'
        expected_result = ['abc', 'array']
        self.assertEqual(filter_by_prefix(strings, prefix), expected_result)

if __name__ == '__main__':
    unittest.main()
```

Within the test class, `TestFilterByPrefix`, the first test, `test_empty_list`, ensures that the function returns an empty list when an empty list of strings is provided. The second test, `test_filter_by_prefix`, verifies that the function returns a list containing only the strings that start with the provided prefix when a list of strings and a prefix are provided. To execute the tests, the `unittest.main()` function is called, which looks for any tests within the script and runs them. 

Note: this script assumes that the function `filter_by_prefix` is defined in a separate file called `filtering.py`. If you intend to execute the script within a Jupyter Notebook or similar environments, please execute the following command to run the test suite in an external terminal:
```python
%%writefile -d -ta test_filter_by_prefix.py filtering.py
``` 
This command automatically creates a file called `test_filter_by_prefix.py` in the same directory as the Notebook and writes the test code onto it. It also automatically edits the script to import the `filter_by_prefix` function from the `filtering.py` file.