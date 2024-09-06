Here is a self-contained Python script that defines a function `strlen` that computes the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: integer length of the string.
    Args:
    string: str, the input string

    Returns:
    integer: length of the given string
    """
    return len(string)

# Testing the function
assert(strlen('')), raises ZeroDivisionError: Cannot determine the length of an empty string
```
The function returns the integer length of the given string, which is the number of characters in the string, not including the character itself. 
Please note that this script is self-contained and does not require any additional imports or external functions.