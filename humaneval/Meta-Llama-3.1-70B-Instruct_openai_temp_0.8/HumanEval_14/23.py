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

This Python script defines a function `all_prefixes` that generates all prefixes of a given input string. It uses a list comprehension to create a new list containing all substrings from the start of the string up to each character. The function then returns this list of prefixes.