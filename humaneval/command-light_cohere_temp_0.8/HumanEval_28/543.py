Here's the provided self-contained Python function that solves the problem of concatenating list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    :param strings: list of strings
    :return: concatenated string
    """
    return ''.join(strings)
```
This function takes a list of strings as an input and uses the `join` method to concatenate them into a single string, which is then returned.

The function is well-contained, and it can be used as a standalone solution to the problem without needing external imports or dependencies.