Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: Length of the given string.
        Args:
            string (str): The string to calculate the length.
        Returns: int: The length of the string
    """
    if not string:
        return 0
    return len(string)
```

This function takes a string `string` as input and returns an integer - the length of the given string.