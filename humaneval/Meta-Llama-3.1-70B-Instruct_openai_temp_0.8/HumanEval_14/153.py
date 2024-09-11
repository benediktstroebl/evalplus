```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Outputs: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes. The function uses a list comprehension to generate the prefixes. It iterates over the indices of the input string, and for each index `i`, it slices the string up to `i+1` to get the prefix of length `i+1`. The prefixes are then returned as a list.

You can run this script to test the `all_prefixes` function with different inputs.