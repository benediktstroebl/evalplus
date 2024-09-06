```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to the specified base.
    Args:
        x: int, Input number
        base: int, Base to which the input number will be converted

    Returns:
        str: The string representation of the input number after conversion to the specified base
    """
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36")
        
    if x < 0:
        x = abs(x)
        
    ret = str(x)
    for c in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        ret = ret.replace(int(c) if c in x else c, c)
        
    return ret

def test_change_base():
    x = 8
    base = 2
    got = change_base(x, base)
    assert got == '1000'
    x = 7
    base = 16
    got = change_base(x, base)
    assert got == '7E4'
    x = -3
    base = 32
    got = change_base(x, base)
    assert got == '-2147483648'

test_change_base()
```