Here is a Python script that contains a self-contained function that solves the problem of finding all prefixes in a string:
```python
from typing import List
import string

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(string[:i] for i in range(1, len(string)+1))

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

test_prefixes()
```

The code defines a function `all_prefixes()` that returns a list of all prefixes in a given string. The function uses a list comprehension with a generator expression to create the desired output. It then passes all test cases, which ensure the correctness of the function.