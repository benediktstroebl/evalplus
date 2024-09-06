Here is a self-contained Python function that solves the problem you described:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]) -> str: List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
```

This function takes a list of strings as an argument and returns a concatenated string by using the `join()` method. The function is self-contained and only uses the input argument to solve the problem.

Here is the expected output when calling the function with a list of strings:
```
'abcd'
```