```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated
    
    Returns:
        str: A single string that is the result of concatenating all strings in the input list
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method returns a string concatenated with the elements of an iterable
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello', ', ', 'world']))  # Output: 'hello, world'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the result of concatenating all strings in the input list. The `join()` method is used to concatenate the strings, and the script includes some test cases to demonstrate the function's behavior.