```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
   
    preferred base is 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'  # Incorrect, 2 does not evenly divide by 8
    >>> change_base(7, 2)
    '111'   # Correct
    """
    return str(x)[str(base):int('0')]
```