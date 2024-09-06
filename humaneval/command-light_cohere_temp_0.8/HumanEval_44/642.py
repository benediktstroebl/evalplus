```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to the base specified.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    if x < 0 or base < 0:
        raise ValueError("Input and base must be non-negative integers")
    s = str(x)
    while len(s) < len(str(x)) // base:
        s = s[-(len(s) % base)] + s[-(len(s) // base) * base]
    return s
```