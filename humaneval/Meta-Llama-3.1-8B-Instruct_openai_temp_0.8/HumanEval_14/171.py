```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string, sorted from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return sorted(prefixes, key=len)

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that generates a list of all prefixes of the input string, sorted from shortest to longest. It uses a loop to generate each prefix by slicing the input string, and the `sorted` function to sort the list of prefixes by their length. The test cases at the end demonstrate the function's behavior.