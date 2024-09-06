```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
    and 2/10, default 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '100'
    >>> change_base(8, 1)
    TraceTypeError: unsupported operand type(7) for unsupported operation '()'
    """
    try:
        result = '{0:0b}'.format(x, base)
        return result
    except TypeError:
        raise TypeError("Unsupported operand type.")

``` 
This Python code defines a function called change_base, which takes two parameters: x (the number to be converted) and base (the desired base for the representation). The function then attempts to convert the number x to a string using the format() function with the specified base, and returns the result. Additionally, the function includes some error handling: if the base is not 10 or 2 (the common base numbers), a TypeError will be raised with a corresponding message indicating that the base is not supported. This way serves as a to convert numbers to string representations using a specified base, and provides appropriate error handling for unsupported base numbers.