Here is a self-contained Python function that solves the problem of concatenating a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string and return it
    """
    return ''.join(strings)
```

This function takes in a list of strings and uses the `join` method to concatenate them into a single string, which it then returns.