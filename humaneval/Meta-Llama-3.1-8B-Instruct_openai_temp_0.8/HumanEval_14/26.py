```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return sorted(prefixes, key=len)

# Test the function
print(all_prefixes('abc'))
print(all_prefixes('python'))
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, sorted from shortest to longest. It does this by iterating over the string, appending each prefix to the list, and finally sorting the list by prefix length.

When you run this script, it will print the prefixes of 'abc' and 'python', demonstrating its functionality.