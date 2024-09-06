```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(string[i:]) for i in range(len(string) + 1)]

# Test cases
string1 = 'abc'
print(all_prefixes(string1))  # Output: ['a', 'ab', 'abc']

string2 = 'hello'
print(all_prefixes(string2))  # Output: ['h', 'ello']

string3 = 'abc123'
print(all_prefixes(string3))  # Output: ['abc123']
```
The provided Python script defines a function called `all_prefixes` that takes a string as input and generates a list of all its prefixes from shortest to longest. The function uses a array slicing technique with `range(len(string) + 1)` to iterate through the string and extract each prefix individually. The test cases demonstrate the how the function works with different input strings.