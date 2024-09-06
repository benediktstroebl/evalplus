Certainly! Here is a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of the given string"""
    if not string:
        return 0
    return len(string)
```
The code defines a function `strlen` that takes a string as input and returns the length of the string. The function is designed with type hints to clearly indicate the expected input parameter (`str: str`) and return value (`int`). The function also includes docstrings to provide explanations and documentation. The function implements the string length using the built-in function `len(string)` which returns the length of the string.