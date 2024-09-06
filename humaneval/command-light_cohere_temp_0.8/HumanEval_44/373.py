```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    if base > x:
        raise ValueError("Input number is smaller than required base.")
    s = str(x)
    for i in range(len(s)):
        if s[i] == '0':
            s = s.replace(format(int(base[0] + i * base[1]), base[2] + i * base[3]))
    return s
```