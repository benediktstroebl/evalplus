```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The behavior of the function is explained using Python's list comprehension and the `startswith` function.

Here is an example of an instance of this function being called:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example uses the function to filter the list of strings given, removing those that do not start with the prefix "a". The function then returns the filtered list, which contains only the strings "abc" and "array". 
This function can be tested successfully using Python's `unittest` module. You can directly verify that the function behaves as expected with example test cases. Here is an example:
```python
import unittest

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filtered_strings(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()
```
In the example, we use Python's `unittest` module to define two test cases, both of which are executed when the `filter_by_prefix()` function is called. The first test case checks if the function correctly handles an empty input list. The second test case checks if the function correctly filters strings that start with the given prefix. The `self.assertEqual()` function checks if the output of the `filter_by_prefix()` function is equal to the expected output for each test case. 
The `unittest.main()` function is called to run the tests. 

This function can be further improved by adding more test cases to cover edge cases, such as input lists with only one string, lists with a huge number of strings, and cases where the prefix is long or short. Adding these cases ensures that the function handles a variety of scenarios without error.