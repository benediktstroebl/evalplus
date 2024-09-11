```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string
    
    Returns:
    List[str]: A list of all prefixes from shortest to longest
    
    Examples:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Get the prefix of the current length
        prefix = string[:length]
        
        # Append the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of all prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. It uses a for loop to generate each prefix by slicing the input string at the current length, and appends each prefix to the list. The function is then tested with two example inputs. 

Note: This script uses Python 3.x syntax, and the `typing` module is used to specify the type of the function's return value. If you are using Python 2.x, you can replace `List[str]` with `list` and remove the `from typing import List` line.