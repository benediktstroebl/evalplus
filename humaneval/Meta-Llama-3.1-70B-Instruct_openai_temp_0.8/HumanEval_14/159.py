```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. It uses a list comprehension to generate the prefixes, iterating over the length of the input string and slicing the string from the start up to each index `i+1`. The example usage at the end demonstrates how to use the function with the string `'abc'`.