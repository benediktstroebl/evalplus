```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string for which prefixes are calculated
    
    Returns:
    List[str]: A list of all prefixes from shortest to longest
    
    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Expected output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from the shortest to the longest. The function uses list comprehension and string slicing (`string[:i+1]`) to generate the prefixes. The `range(len(string))` generates indices from 0 to the length of the string minus one, and for each index `i`, it takes the substring from the start of the string up to `i+1`.