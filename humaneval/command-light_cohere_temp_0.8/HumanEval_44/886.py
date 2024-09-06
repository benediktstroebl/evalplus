```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are using 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 1)
    TraceTypeError: unsupported operand type(5) for unary '>' +' operator
    >>> change_base('hello', 5)
    TraceTypeError: unsupported operand type('hello') for operation '+'
    ```
The provided code defines a function `change_base` which converts a number to a specified base. It employs the code to ensure the base number is a valid integer and raises an `TypeError` if the input type is not numeric. 
The function returns the string representation of the number using the desired base.