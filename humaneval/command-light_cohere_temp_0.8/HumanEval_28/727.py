Here's a self-contained Python function that solves the problem of concatenating list of strings:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string and return it.
    :param strings: list of string, returns: concatenated string
    """
    return ''.join(strings)
```
The code defines a function called `concatenate` which takes a list of strings as input and returns the concatenated string. It uses the convenient `.join()` method to concatenate the strings into a single string.