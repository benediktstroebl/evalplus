```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function utilizes list comprehension and a generator expression to filter out the relevant strings from the input list. 

To test this function, you can use the following code:
```python
import unittest

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_matching_strings(self):
        input_list = ['abc', 'bcd', 'cde', 'array']
        expected_output = ['abc', 'array']
        self.assertEqual(filter_by_prefix(input_list, 'a'), expected_output)

    def test_non_matching_strings(self):
        input_list = ['123', 'bcd', 'xyza', 'foo']
        prefix = 'xx'
        expected_output = []
        self.assertEqual(filter_by_prefix(input_list, prefix), expected_output)

if __name__ == '__main__':
    unittest.main()
```

This test suite includes three distinct tests to verify the correctness of the `filter_by_prefix` function. In particular, it checks the result against an empty list, verifies matching strings, and confirms that non-matching strings are correctly filtered out.  The `unittest.main()` function is used to discover and run the tests. 

To run the test suite, save the code into a file (e.g., `test_filter_by_prefix.py`) and execute the file in your Python environment. 

This approach ensures that the `filter_by_prefix` function works correctly and aligns with the expected behavior, as outlined in the original problem statement.