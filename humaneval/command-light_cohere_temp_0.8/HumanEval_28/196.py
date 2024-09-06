Here is a Python script that solves the problem you described:

```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        string
    """
    return "".join(strings)
```

This script defines a function called `concatenate` that takes in a list of strings and returns a concatenated string. It uses the necessary list comprehension to convert the list of strings into a single string and then returns that concatenated string.