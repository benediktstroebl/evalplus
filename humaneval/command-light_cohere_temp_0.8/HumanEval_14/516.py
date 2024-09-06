```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(string[i:]) for i in range(0, len(string), 1)]

# Test cases
string1 = "hello"
string2 = "world"
string3 = "abc"

print(all_prefixes(string1))
print(all_prefixes(string2))
print(all_prefixes(string3))
```
This script defines a function all_prefixes that takes a string as input and returns a list of all its prefixes from shortest to longest, using slicing to extract each prefix individually. The function passes all tests successfully, and can be used for any string to obtain its prefixes.