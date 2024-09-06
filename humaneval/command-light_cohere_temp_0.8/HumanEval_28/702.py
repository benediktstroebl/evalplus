Here's the self-contained Python function that solves the problem of concatenating list of strings:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
```

This function takes a list of strings as input and uses the `join` method to concatenate them into a single string. 
It's a self-contained solution that can be easily copied and used in other projects.