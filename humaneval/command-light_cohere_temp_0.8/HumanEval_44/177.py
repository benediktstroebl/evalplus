```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    return str(x).check_base(x, base)[0]

def check_base(x: int, base: int):
    """
    Check whether x can be represented in base base.
    >>> check_base(8, 10) == True
    True
    >>> check_base(2, 2) == True
    True
    >>> check_base(3, 10) == False
    True
    """
    return x == int(str(x)[base])
```