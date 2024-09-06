```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number x to the base b.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(-8, 2) == '128'
    True
    >>> change_base(10, 3) == '00030'
    False
    >>> change_base(15, 10) == '15'
    False
    """
    if base < 2 or base > 36:
        raise ValueError("base should be between 2 and 36")
    
    if base == 10:
        return str(x)
    
    if base == 2:
        return str(int(x) * pow(base, 32 - 4, base))
    
    num = x
    base_str = str(base)
    
    for i in range(len(base_str)):
        num = num * 10**(base_str[i] - 4)
    
    return str(num)
```