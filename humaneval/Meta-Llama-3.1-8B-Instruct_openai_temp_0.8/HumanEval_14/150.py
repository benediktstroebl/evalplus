### Prefixes of a String
#### Python Script

```markdown
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes in order from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Loop through the string, adding each prefix to the list
    for i in range(1, len(string) + 1):
        # Slice the string up to the current index to get the prefix
        prefix = string[:i]
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. The function uses a loop to generate each prefix by slicing the input string up to the current index. The list of prefixes is then returned. The example usage section demonstrates how to use the function with a few sample strings.