```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of prefixes.

    Examples:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script uses list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` slices the string from the beginning to the index `i+1`, effectively creating a prefix of length `i+1`. The range of `i` goes from 0 to `len(string)-1`, ensuring that all prefixes are generated.