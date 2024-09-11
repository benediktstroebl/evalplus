```markdown
### All Prefixes of a String

This script defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of the input string.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes of the input string.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('python'))  # Output: ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']
```

This script works by iterating over the range of possible prefix lengths (from 1 to the length of the input string), and appending the substring of the input string up to each length to the list of prefixes. The resulting list is then returned. The example usage demonstrates the function's behavior with different input strings.