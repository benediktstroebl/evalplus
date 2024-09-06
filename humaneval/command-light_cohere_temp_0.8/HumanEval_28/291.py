```python
def concatenate(strings: List[str]) -> str:
    """
    Function to concatenate list of strings into a single string.

    Args:
        strings (List[str]): List of strings to be concatenated

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
``` 
This code defines a Python function called `concatenate` which takes a list of strings as an argument and returns the concatenated string as its output. 
The `strings` list is converted into a single string using the `join` method, which iterates over the strings in the list and joins them together with a space character.