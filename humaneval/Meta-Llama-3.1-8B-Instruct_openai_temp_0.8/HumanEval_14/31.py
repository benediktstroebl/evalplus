```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): Input string.

    Returns:
        List[str]: List of all prefixes.
    """
    result = []  # Initialize an empty list to store the prefixes
    for i in range(len(string) + 1):  # Iterate over the string with indices from 0 to n (where n is the length of the string)
        prefix = string[:i]  # Get the prefix of length i
        result.append(prefix)  # Add the prefix to the list
    return result  # Return the list of prefixes

# Test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. It uses a simple loop to iterate over the string, getting each prefix by slicing the string up to the current index. The prefixes are then collected in a list, which is returned at the end. The script includes a test case to demonstrate the function's behavior.