```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    >>> return ''.join(strings)
    """

# tests
import unittest

class TestLongest(unittest.TestCase.TestCase):
    def test_strings(self):
        self.strings = ['a', 'bb', 'ccc', 'd', 'e', 'f']
        self.long = longest(self.strings)
        expected_ return 'ccc'
    assert self.long == 'ccc'

if __name__ == '__main__':
    unittest.main()
```

This function takes a list of strings and returns the longest string. It is tested using the unittest to ensure the function works as expected.