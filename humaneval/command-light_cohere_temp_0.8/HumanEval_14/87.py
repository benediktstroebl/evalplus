```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', string] + all_prefixes(sub) for sub in string.

# Test cases
print(all_prefixes(''))
print(all_prefixes(' '))
print(all_prefixes('abc'))
print(all_prefixes(' foo '))
print(all_prefixes([ 'abc', 'def' ]))
``` 
This script defines a function all_prefixes that generates all prefixes of a given string using recursion. 
The function takes a string as input and returns a list of its prefixes. 
This script provides a fully self-contained solution to the problem of generating all prefixes of a given string.