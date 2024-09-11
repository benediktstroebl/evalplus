### Concatenating a List of Strings into a Single String

Here's a Python function to solve the problem using the `join()` method, which is more efficient than using the `+` operator for string concatenation.

```markdown
### Code

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Check if input is a list
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings.")
    
    # Check if all elements in the list are strings
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")
    
    # Use join() method to concatenate all strings in the list
    return ''.join(strings)

# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

### Explanation

1.  The function `concatenate(strings: List[str]) -> str` takes a list of strings as input and returns a single string.
2.  It first checks if the input is a list and if all elements in the list are strings. If not, it raises a `ValueError`.
3.  It uses the `join()` method to concatenate all strings in the list. The `join()` method takes an iterable of strings as an argument and returns a single string that is the concatenation of all input strings.
4.  The `join()` method is more efficient than using the `+` operator for string concatenation because it only creates one new string, whereas using the `+` operator creates a new string in each iteration.

### Example Use Cases

The example usage at the end of the script shows how to use the `concatenate()` function to concatenate empty list and a list of strings.