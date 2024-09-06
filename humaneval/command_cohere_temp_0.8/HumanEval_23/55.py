```python
def strlen(string: str) -> int:
    """ Return length of given string
    :param string: Input string
    :return: Length of the input string
    """
    return len(string)
```

This Python function uses the built-in `len()` method to determine the length of any given string. It performs as expected against an empty string and a string of three characters, as shown in the provided docstring. 

You can include this code within a Python script, and it will successfully compute the length of any given string. Simply call the `strlen` function anywhere on its own line, passing a string as an argument, and it will return the length of that input. 

For example, running `strlen('abc')` will yield the output `3`.