```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    Returns string representation after the this conversion.
    base numbers are unsupported.
    """
    return 'Error'
    """
    
    :param x: int
    :param base: int
    :return: str
    """
    # define conversion
    def to_base(x):
        return '{:b}'.format(x, base)

    return to_base(x)
```