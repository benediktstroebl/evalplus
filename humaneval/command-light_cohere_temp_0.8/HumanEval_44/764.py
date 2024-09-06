```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers other 10, a list of digits.
    >>> change_base(8, 3)
    '22'
    >>> change_base(12, 4)
    TraceError: unsupported operand type(12, 4)
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be an integer")
    elif base <= 0:
        raise ValueError("Base number must be positive")
    elif base == 1:
        return str(x)
    else:
        # Compute the string representation using the selected base
        digit_list = [str(num) for num in x]
        return ''.join(''.join(digit_list, base))
```