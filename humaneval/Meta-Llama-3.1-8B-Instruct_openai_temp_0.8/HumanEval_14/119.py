```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string from which all prefixes are generated.
    
    Returns:
    List[str]: A list of all prefixes of the input string in order from shortest to longest.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))
```

This Python script defines a function `all_prefixes` that generates all prefixes of a given string and returns them in a list. The function uses slicing (`string[:i+1]`) to extract substrings of increasing length up to the length of the string. The list comprehension iterates over the indices from 0 to the length of the string, generating each prefix as it goes. The result is printed out when you run the script.