```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This algorithm uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. In this case, it iterates over each element `s` in the `strings` list and includes it in the new list if it contains the `substring`. 

To run the tests for this function, you can use the following code:
```python
import unittest

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_contains_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_does_not_contain_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b'), ['abc', 'cde', 'array'])

if __name__ == '__main__':
    unittest.main()
```

This code uses the `unittest` module to define three test cases:
1. `test_empty_strings`: Tests whether the function returns an empty list when an empty list of strings is provided.
2. `test_contains_substring`: Tests whether the function returns the correct list of strings that contain the given substring.
3. `test_does_not_contain_substring`: Tests whether the function returns the correct list of strings that do not contain the given substring.

The `unittest.main()` function is used to discover and run the tests. When you run this test case, Python will execute the tests and provide you with a detailed report on whether the tests pass or fail.