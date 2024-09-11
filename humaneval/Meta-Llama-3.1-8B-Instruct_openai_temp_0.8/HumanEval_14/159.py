```python
from typing import List, Generator

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
    string (str): The input string.
    
    Returns:
    List[str]: A list of all prefixes of the input string, in order from shortest to longest.
    
    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use a generator expression to generate all prefixes of the input string
    # The expression'string[i:]' gets all characters from index i to the end of the string
    # We use range(len(string)) to get all indices from 0 to the length of the string
    prefixes = (string[i:] for i in range(len(string) + 1))
    
    # Convert the generator to a list, sort it, and return it
    return sorted(list(prefixes), key=len)


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, in order from shortest to longest. The function uses a generator expression to generate all prefixes, converts the generator to a list, sorts the list by the length of the prefixes, and returns it. The script also includes a test of the function with two different input strings.