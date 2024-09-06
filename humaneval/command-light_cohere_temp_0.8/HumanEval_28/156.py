```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
```
The code defines a function called `concatenate` that takes in a list of strings as an argument. The function uses the string formatting with the `join()` function to create a new string that contains the values of the input list. 

This solution is self-contained, and it passes the test with the provided input values.