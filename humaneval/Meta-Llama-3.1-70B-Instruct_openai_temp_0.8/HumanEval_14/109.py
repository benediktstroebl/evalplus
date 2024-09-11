```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes an input string and returns a list of all its prefixes, from the shortest to the longest. The function uses list comprehension to generate the prefixes. The `string[:i+1]` expression creates a substring from the start of the string to the current index `i+1`. The `range(len(string))` generates indices from 0 to the length of the string minus one.

You can run the script, and it will print the list of prefixes for the input string 'abc'.