Here's a self-contained Python script that solves the problem of concatenating strings in Markdown code blocks, along with unit tests using the `unittest` library:
```python
import unittest
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

class TestConcatenate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual('[]')
        result = concatenate([])
        self.assertEqual(result)
        assert result == ''

    def test_single_item(self):
        self.assertEqual(['a'])
        result = concatenate(['a'])
        self.assertEqual(result)
        assert result == 'a'

    def test_multiple_items(self):
        self.assertEqual(['a', 'b', 'c'])
        result = concatenate(['a', 'b', 'c'])
        self.assertEqual(result)
        assert result == 'abc'

if __name__ == '__main__':
    unittest.main()
```

In this script, we define a `concatenate` function that takes a list of strings and concatenates them into a single string. We then create a test cases for the function: empty list, single item, and multiple items. The `unittest` library is used to define and run the tests, and the test cases assert that the function's output is correct for the given input.