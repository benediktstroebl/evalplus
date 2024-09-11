```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from the shortest to the longest. The function uses a list comprehension to generate the prefixes by slicing the input string at each position from 1 to the length of the string. The example usage demonstrates how to call the function with the input string 'abc' and prints the resulting list of prefixes.