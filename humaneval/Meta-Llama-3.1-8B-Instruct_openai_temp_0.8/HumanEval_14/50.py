```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
    string (str): The input string.
    
    Returns:
    List[str]: A list of all prefixes of the input string.
    
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. The function uses a `for` loop to iterate over the indices of the string (from 1 to the length of the string), and for each index, it appends a slice of the string up to that index to the list of prefixes. Finally, it returns the list of prefixes.