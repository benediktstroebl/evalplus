```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string for which all prefixes are to be generated.
    
    Returns:
    List[str]: A list of strings representing all prefixes of the input string.
    """
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the length of the input string
    for i in range(1, len(string) + 1):
        # Append the prefix of the current length to the list
        prefixes.append(string[:i])
    
    # Return the list of all prefixes
    return prefixes

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Another example
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```