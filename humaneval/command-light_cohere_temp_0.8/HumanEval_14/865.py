Here is a Python script that contains a self-contained function that solves the problem of finding all prefixes of a given string:
```python
from typing import List
import re

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [prefix for prefix in re.findall('.*? sm', string)
    r'a.*c' )

# Test cases
print(all_prefixes('abc')) # ['a', 'ab', 'abc']
print(all_prefixes(''))   # []
``` 
This script defines a function all_prefixes that takes a string as input and returns a list of all prefixes of that string. The function uses the re.findall to generate all list of all possible prefixes of the string, from shortest to longest.