```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes of the input string
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        # Slice the string to get the prefix
        prefix = string[:i]
        prefixes.append(prefix)
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the input string, from shortest to longest. The function uses a for loop to iterate over the length of the input string, and for each iteration, it slices the string to get the prefix and adds it to the list of prefixes. The function is then tested with two example strings.