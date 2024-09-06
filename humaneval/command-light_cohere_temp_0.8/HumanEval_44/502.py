```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    :param x: int or float - input number
    :param base: int - base to convert to
    :return: string representation of x in new base
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an integer or float")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if base == 10:
        return str(x)
    base_list = [10,  12,  15,  17,  20,  23,  25,  28,  31,  32,  33,  34,  36]
    if base not in base_list:
        raise ValueError("Invalid base")
    result = str(x, base)
    return result

def test_change_base():
    """Test the change_base function"""
    assert change_base(45, 10) == '450'
    assert change_base(3.5, 10) == '35'
    assert change_base(8, 2) == '1000'
    assert change_base(-45.2, 10) == '-450.2'
    supports the recommended test to see how the function behaves.

test_change_base()
```