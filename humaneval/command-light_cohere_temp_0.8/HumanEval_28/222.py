Here is a Python script that solves the problem of concatenating a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return "".join("".join(strings))
```
This function takes a list of strings as input and concatenates them into a single string, returning that result. 
It uses the str.join() method to concatenate the strings in a list into a single string.