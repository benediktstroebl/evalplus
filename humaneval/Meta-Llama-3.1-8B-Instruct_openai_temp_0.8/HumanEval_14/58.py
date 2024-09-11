```markdown
## Prefix Generation Script

This Python script generates all prefixes of a given string from shortest to longest.

### Code

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string for generating prefixes.

    Returns:
        List[str]: A list of prefixes in order from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):  # Loop through all possible prefix lengths
        prefixes.append(string[:i])  # Append the prefix to the list
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

### Explanation

This script defines a function `all_prefixes` that generates all prefixes of a given string. It uses a loop to iterate through all possible prefix lengths, appending each prefix to the `prefixes` list. The function returns the `prefixes` list in order from shortest to longest.

The script also includes example usage and a docstring that explains the function's behavior and usage.