```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated
    
    Returns:
        str: The concatenated string
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method returns a string concatenated with the elements of an iterable
    return ''.join(strings)

# Example usage:
strings_list = ['Hello','', 'World', '!']
print(concatenate(strings_list))  # Outputs: 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The `join()` method is used to concatenate all strings in the list. The script also includes example usage of the function.