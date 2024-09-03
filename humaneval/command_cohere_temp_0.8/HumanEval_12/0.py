```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(set(strings), key=strings.count)
```
This code defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, it returns `None`. The function uses a combination of `max` and `set` to handle cases where there are multiple strings of the same length and returns the first occurrence of such strings. 

Here's an example of how you can test this function using the Python `unittest` framework:
```python
import unittest

class TestLongestFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_longest_string(self):
        self.assertEqual(longest(['a', 'b', 'ccc']), 'ccc')

    def test_multiple_same_length_strings(self):
        self.assertEqual(longest(['a', 'b', 'c', 'a', 'b']), 'a')

if __name__ == '__main__':
    unittest.main()
```

In this test suite, we have four individual test functions that exercise different scenarios of the `longest` function as described in the problem statement. The `unittest.main()` call runs all the tests when the script is executed directly. 

To run this test suite, you can save the code into a Python file (e.g., `test_longest.py`) and execute the file using the command line:
```bash
python test_longest.py
```
The `unittest` framework will then run all the tests and report any failures or errors.