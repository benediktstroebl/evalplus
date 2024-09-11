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
    prefixes = []  # Initialize an empty list to store prefixes
    
    # Generate all prefixes by slicing the string from index 0 to i
    for i in range(len(string) + 1):  
        prefixes.append(string[:i])  # Add the prefix to the list
    
    return prefixes  # Return the list of prefixes

# Testing the function
print(all_prefixes('abc')) 
# Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes in order from shortest to longest. The function uses a for loop to generate all prefixes by slicing the string at each index from 0 to the length of the string. The generated prefixes are then appended to a list, which is returned at the end. The code includes a test case to demonstrate the function's usage.