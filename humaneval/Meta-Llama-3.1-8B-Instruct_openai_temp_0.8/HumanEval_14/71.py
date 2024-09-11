```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes in order from shortest to longest
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Loop through the string with two nested loops to generate all prefixes
    for i in range(1, len(string) + 1):
        # Slice the string up to the current index to get the prefix
        prefix = string[:i]
        
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```