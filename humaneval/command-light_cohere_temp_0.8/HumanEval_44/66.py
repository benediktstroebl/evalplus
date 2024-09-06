```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base represented by base.
    Return the string representation of the number in the given base.
    """
    numbers beyond base base may for which x cannot be represented in
    the given base, will be returned as they are.
    """
    base can be any of the number 10 (decimal), 2 (binary), or 16 (hexadecimal).
    """
    if x < 0 or base < 2 or base > 16:
        return x
    if base == 10:
        return str(x)
    elif base == 2:
        return str(x, 'binary')
    elif base == 16:
        return str(x, 'hexadecimal')
    else:
        return str(x, base)

def test_change_base():
    """
    Test the change_base function with various arguments and base values.
    """
    expected output is 1, 2, 10, 3, 8, 16, 22, 1000, 111, and True.
    """
    x = 8
    base = 3
    result = change_base(x, base)
    print(result)
    assert result == '22'
    x = 8
    base = 2
    result = change_base(x, base)
    print(result)
    assert result == '1000'
    x = 7
    base = 2
    result = change_base(x, base)
    print(result)
    assert result == '111'
    assert change_base(10, 2) == '1000'
    assert change_base(16, 2) == '10000'
    assert change_base(7, 2) == '111'
    assert change_base(8, 10) == '8'
    assert change_base(8, 2) == '80'
    assert change_base(7, 16) == '7A'
    assert change_base(7, 2) == '7111'
    assert change_base(16, 16) == '10000'
    assert change_base(10, 16) == '10100'
    assert change_base(3, 2) == '10'
    assert change_base(16, 3) == '101000'
    assert change_base(8, 3) == '8'
    assert change_base(7, 2) == '7111'
    assert change_base(7, 16) == '7A10000'
    assert change_base(8, 16) == '8000'
    assert change_base(7, 2) != '81'
    assert change_base(7, 16, 2) == '7111'
    assert change_base(10, 16, 2) == '10000100'
    assert change_base(16, 2, 2) == '16'
    assert change_base(16, 16, 16) == '1616161616'
    assert change_base(3, 16, 16) == '3E16161616'
    assert change_base(-8, 16) == '-8E16161616'
    assert change_base(8, -16) == '-8'
    assert change_base(-7, 2) == '-7'
    assert change_base(-7, 16) == '-7A'
    assert change_base(-16, 2) == '-16000'
    assert change_base(-16, 16) == '-1616161616'
    assert change_base(0, 16) == '0'
    assert change_base(0, -16) == '0'