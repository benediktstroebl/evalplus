```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', 'abc']  # short to long order

# Test cases
test_prefixes = [
    dict(zip(('very', 'long'), [
        all_prefixes('very'),
        all_prefixes('long'),
    ]))
]

if __name__ == '__main__':
    unittest.loadTests(test_prefixes)
    unittest.test()()  # Run the all the test cases for prefixes
```