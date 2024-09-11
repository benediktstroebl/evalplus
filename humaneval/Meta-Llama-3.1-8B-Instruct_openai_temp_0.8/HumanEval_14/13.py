**Prefix Generation Script**
==========================

Below is a Python script that generates all prefixes of a given string.

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
    return prefixes


# Example usage:
if __name__ == "__main__":
    string = 'abc'
    prefixes = all_prefixes(string)
    print(prefixes)
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes. It then demonstrates the function's usage on the string `'abc'`.

**Explanation:**

1. We iterate over the indices of the string from 1 to the length of the string (inclusive).
2. At each index `i`, we append the substring from the start of the string to `i` to the `prefixes` list.
3. Finally, we return the `prefixes` list.

This solution has a time complexity of O(n), where n is the length of the input string, because we only iterate over the string once.