## Prefix Generation Script
### Overview

This Python script generates all prefixes of a given string from shortest to longest.

### Code

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of all prefixes

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for length in range(1, len(string) + 1):
        prefixes.append(string[:length])
    return prefixes


# Example usage
if __name__ == "__main__":
    string = 'abc'
    prefixes = all_prefixes(string)
    print(prefixes)
```

### Usage

*   Save the script above in a file with a `.py` extension, for example, `prefixes.py`.
*   Run the script using Python: `python prefixes.py`.
*   The script will print the list of prefixes for the string `'abc'`.

### Explanation

The `all_prefixes` function generates all prefixes of a given string by iterating over the string's length from 1 to the string's total length. It uses Python's slicing feature to create a prefix of the current length and adds it to the `prefixes` list. Finally, it returns the `prefixes` list.

In the example usage section, the script calls `all_prefixes` with the string `'abc'` and prints the result.