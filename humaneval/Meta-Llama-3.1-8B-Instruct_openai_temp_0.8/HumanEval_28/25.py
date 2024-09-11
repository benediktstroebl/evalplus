```markdown
### Concatenate List of Strings into a Single String

This Python script uses the built-in `join()` method to concatenate a list of strings into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to concatenate.

    Returns:
        str: The concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Check if input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings.")
    
    # Check if all elements in the list are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements in the list must be strings.")
    
    # Use join() method to concatenate the list of strings
    return ''.join(strings)

# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    ```
```