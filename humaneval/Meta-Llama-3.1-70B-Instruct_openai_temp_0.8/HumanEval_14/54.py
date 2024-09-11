```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of the input string by using list comprehension to slice the string from the beginning to each index `i+1`, where `i` ranges from 0 to the length of the string. The result is a list of all prefixes, from shortest to longest. The script includes a docstring with an example usage of the function, and also includes a print statement at the end to demonstrate the function's output.