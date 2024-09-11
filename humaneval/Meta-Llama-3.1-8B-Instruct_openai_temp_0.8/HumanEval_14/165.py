```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes in the input string, from shortest to longest
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('abcdef'))  # ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
```

This script uses a single loop to generate all prefixes of the input string by slicing the string for each possible length from 1 to the length of the string. The resulting prefixes are then returned in a list.