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
    return [string[:i + 1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, we use a list comprehension to generate all prefixes of the input string. The `string[:i + 1]` expression generates a prefix of length `i + 1` by slicing the string from the beginning up to, but not including, index `i + 1`. The `range(len(string))` expression generates indices from 0 up to, but not including, the length of the string, which allows us to generate prefixes of all possible lengths.