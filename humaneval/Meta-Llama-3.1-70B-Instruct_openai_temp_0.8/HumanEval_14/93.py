```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of all prefixes of the input string
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script defines the `all_prefixes` function, which uses a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression generates a substring of `string` from the start up to the `(i+1)`th character. The `range(len(string))` expression generates indices `i` from 0 up to the length of `string`, which are used to generate all prefixes.