Here's a Python script that solves the problem:
```markdown
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): Input string.

    Returns:
        List[str]: List of prefixes of the input string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```
This script uses a list comprehension to generate all prefixes of the input string. The outer loop generates indices from 0 to the length of the string, and the string slicing operation `string[:i+1]` generates prefixes of varying lengths. The `range(len(string))` function generates the indices, and the `+1` is used to include the last character in the prefix.