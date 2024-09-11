```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: List of all prefixes
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script uses list comprehension to generate all prefixes of the input string. It iterates over the range of the length of the string, slicing the string from the beginning to the current index `i+1` to get each prefix. The prefixes are then returned as a list.