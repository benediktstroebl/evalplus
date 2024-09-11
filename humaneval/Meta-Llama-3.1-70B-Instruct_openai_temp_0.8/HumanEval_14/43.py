```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. It uses a list comprehension to generate the prefixes by slicing the input string from the start up to each index `i` in the range from 1 to the length of the string (inclusive). The example usage at the end demonstrates how to call the function with the input string 'abc' and print the resulting list of prefixes.