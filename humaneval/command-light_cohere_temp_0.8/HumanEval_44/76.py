```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers other 10
   
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Check base
    assert base == 10, f"Base must be 10, was {base} instead"

    # Perform the conversion
    assert round(x) == str(x)

    return x
```