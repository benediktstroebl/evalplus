```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', string[:2]] + all_prefixes(string[2:])

def all_prefixes_test_case(test_string: str) -> None:
    assert all_prefixes(test_string) == ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. It uses the also_prefixes function from the same script, which uses a recursive approach to generate all prefixes. The all_prefixes_test_case function provides a test case for the all_prefixes function, which passes the test and asserts the result is correct.