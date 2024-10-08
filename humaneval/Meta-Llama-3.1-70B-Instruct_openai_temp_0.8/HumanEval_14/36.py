```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Expected output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from the shortest to the longest. The function uses a list comprehension to generate the prefixes by slicing the input string up to each index `i+1` in the range of the string's length.