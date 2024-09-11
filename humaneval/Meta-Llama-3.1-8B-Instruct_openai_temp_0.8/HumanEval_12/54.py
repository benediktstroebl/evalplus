```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list or None if the list is empty.
    """
    # Check if the list is empty
    if not strings:
        # If the list is empty, return None
        return None
    
    # Use the max function with a key to find the longest string
    # The key function returns the length of each string
    # If there are multiple strings of the same length, max will return the first one
    longest_str = max(strings, key=len)
    
    # Return the longest string
    return longest_str

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function called `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, it returns `None`. The function uses the `max` function with a key function to find the longest string, which makes the code concise and efficient. The test cases are included to verify the correctness of the function.