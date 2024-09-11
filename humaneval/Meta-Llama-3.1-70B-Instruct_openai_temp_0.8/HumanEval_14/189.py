```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from the shortest to the longest. The function uses a list comprehension to generate the prefixes. It iterates over the range of the length of the input string, slicing the string up to the current index `i` plus one (`i+1`) to generate each prefix. The resulting list of prefixes is then returned by the function.