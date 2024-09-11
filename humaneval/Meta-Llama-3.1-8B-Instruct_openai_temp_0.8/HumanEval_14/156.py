```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes of the input string
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('a'))  # Output: ['a']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string. The function uses a list comprehension to generate the prefixes by slicing the input string from the start to each possible position. The resulting list is then returned. The script also includes some example usage of the function.