```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a concise way of expressing a for loop in Python. 

To see how this function works in the real-world, let's consider a use case where we have the following list of strings: `["abc", "bcd", "cde", "array"]`, and we want to filter this list to include only those strings that start with the prefix, "a". 

The function would return `["abc", "array"]`, as these are the only two strings in our input that start with the prefix, "a". 

This function is also compatible with typing modalities in Python, which allows for better documentation and easier use of the function. 

If you would like to test this function to see if it passes any edge cases, feel free to use Python's built-in `unittest` module, which can be used to test the function-

```python
import unittest

class TestFilterByPrefix(unittest.TestCase):
    def test_filter_by_prefix(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar'), ['array'])

    def test_empty_string(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], ''), [])

    def test_non_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'xx'), [])

if __name__ == '__main__':
    unittest.main()
```

This piece of code provides three unit tests for the `filter_by_prefix()` function using Python's `unittest` module. In the first test, we test the function by passing an empty list of strings and the prefix, 'a'. The expected output is an empty list, which is what the function returns. The second test is similar, but we include a list of strings that contains two strings that start with the prefix, 'a', along with some other strings that don't match the prefix. The function is expected to return a list with only the strings that start with the prefix. Finally, the third test ensures that the function returns an empty list when an empty prefix is used on a non-empty list of strings. 

To run these tests, you can use the `unittest` module, which will run each test case separately and report any failures or errors. 

This way, you can easily verify whether or not the `filter_by_prefix()` function works correctly and behaves as expected.