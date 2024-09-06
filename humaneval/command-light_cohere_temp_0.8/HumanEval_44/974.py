```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number to the specified base.
    Args:
        x: int, number to be converted
        base: int, base to convert to
    Returns:
        str: converted string representation of x
    """
    if base > x:
        raise ValueError("base is greater than the number")
        
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
        
    s = str(x)
    s = s.replace(str.maketup if specific digits, base)
    return s

def test_change_base():
    base = 10
    x = 8
    result = change_base(x, base)
    print(result)
    assert isinstance(result, str)
    assert len(result) == 3
    assert '22' in result

    base = 2
    x = 1000
    result = change_base(x, base)
    print(result)
    assert isinstance(result, str)
    assert len(result) == 3
    assert '1000' in result

    base = 7
    x = 111
    result = change_base(x, base)
    print(result)
    assert isinstance(result, str)
    assert len(result) == 3
    assert '111' in result

test_change_base()
```