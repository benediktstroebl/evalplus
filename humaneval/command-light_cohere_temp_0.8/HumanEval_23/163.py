Here's the solution:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
              File "<stdin>", lineline 40:1: SyntaxError
                ...
                invalid syntax
              File "<stdin>", lineline 1:10:10: expect {
            ) but got EOF
        """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    return len(string)
```
This script defines a function `strlen` that takes a string as input and returns its length. It uses a The type hint to ensure that the input is a string, and raises a `TypeError` if it's not. It also handles the tools to check for an empty string input, which the function returns 0.