```markdown
### Problem: Generate All Prefixes of a String

#### Solution: Python Script to Generate All Prefixes of a String

```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): Input string
    
    Returns:
        List[str]: List of all prefixes of the input string
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        prefixes.append(prefix)
    return prefixes


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

#### Explanation:

This script uses a simple loop to generate all prefixes of the input string. The `range(1, len(string) + 1)` generates numbers from 1 to the length of the string. The `string[:i]` expression gets the prefix of the string up to the current index `i`. The prefix is then appended to the `prefixes` list. Finally, the function returns the list of prefixes.

The example usage demonstrates how to use the `all_prefixes` function with different input strings.