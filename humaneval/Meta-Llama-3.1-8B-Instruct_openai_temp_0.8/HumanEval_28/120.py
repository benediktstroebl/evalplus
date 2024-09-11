### Concatenating List of Strings into a Single String

Below is a self-contained Python script that defines a function to concatenate a list of strings into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated.
    
    Returns:
        str: The concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate the strings
    return ''.join(strings)

# Example usage:
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

In this script, the `concatenate` function uses the `join()` method to concatenate the strings in the input list. The `join()` method is a string method that returns a string concatenated with the elements of an iterable. In this case, we use it to concatenate the strings with an empty string as the separator.