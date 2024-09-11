```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes in the order from shortest to longest.
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this script, we use a simple loop to generate all prefixes of the input string. The loop iterates over the length of the string, and in each iteration, it appends a substring of the string from the beginning to the current index to the list of prefixes. The result is a list of all prefixes in the order from shortest to longest.