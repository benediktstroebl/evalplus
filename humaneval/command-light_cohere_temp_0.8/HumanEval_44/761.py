```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another.
    :param x: int - Input number
    :param base: int - Base to which the input number is converted
    :return: string representation of the converted number
    """
    if x < 0 or base < 2:
        raise ValueError("Base must be greater than zero and greater than or equal to 2")
        
    # Ensure base is not 10
    if base == 10:
        base = int('11')
    
    # Special case for zero
    if x == 0:
        return '0'

    # Perform the conversion
    return format(x, int(base))

def test_change_base():
    """
    Test the change_base function
    """
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(-8, 2) == '-1000'
    assert change_base(7, 20) == '111'
    assert change_base(10, 11) == '110'
    assert change_base(123, 2) == '00230300'
    
    # Raise exception for invalid base
    with pytest.raises(ValueError):
        change_base(10, 10)

test_change_base()
```