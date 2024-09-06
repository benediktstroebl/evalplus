```python
def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function using unittest module
from unittest import TestCase
from unittest.py import main, unittest

class TestFilterIntegers(TestCase):
    def test_filter_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}]))
        self.assertEqual(filter_integers(['a', 3.14, 5]))
        self.assertEqual(filter_integers([10, 'a', 2, 'b', [1, 2]]))

if __name__ == '__main__':
    unittest.main()
```