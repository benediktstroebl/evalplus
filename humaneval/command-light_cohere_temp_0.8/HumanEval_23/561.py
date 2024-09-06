Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)
```
This code defines a function `strlen` that takes a string as an argument and returns its length.  The way the **string** is a type hint in Python that indicates that the function is expecting a string to be passed as an argument. The function then uses the **len(string)** to directly get its length, which is the number of characters in the string, and returns this value.