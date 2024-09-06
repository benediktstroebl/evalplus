```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Returns a basic string representation after conversion.
    base numbers less 10 orbase digits.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Convert number to string using base number
    number_str = ''.join(str(x) for x in range(base))
    # Join with separator
    return number_str
```