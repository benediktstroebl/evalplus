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
    return sorted(prefixes)

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string, from the shortest to the longest. It achieves this by iterating over the indices of the string, slicing the string up to each index, and appending the resulting prefix to a list. The list is then sorted before being returned.

In the example usage, we call `all_prefixes` with the strings 'abc' and 'hello', and print the resulting lists of prefixes.