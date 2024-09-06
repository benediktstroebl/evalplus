```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of the input number x to base base.
    :return string representation after conversion
    """
    Args:
        x (int): The number to be converted
        base (int): The base to which the number will be converted

    Returns:
        str: The string representation of the number in the specified base
    """
    if base > 0 and base <= 36:
        return f'{x:{base}}'
    else:
        raise ValueError("Invalid base value")

def test_change_base():
    """Unit tests for the change_base function"""
    assert change_base(8, 3) == '22'
    assert change_base(7, 5) == '107'
    assert change_base(-5, 2) == '-20'
    assert change_base(10, 9) == '9999'
    assert change_base(123, 0) == '1'
    assert change_base(123, 1) == '123'
    assert change_base(123, 35) == 'XBW123'
    assert change_base(10, 11) == '?'
    assert change_base(None, 4) == '?'
    assert change_base(3, 42) == '?'
    assert change_base(-123, 20) == '-6000'
    assert change_base(123, -3) == '-403'

if __name__ == "__main__":
    test_change_base()
```
The provided code defines a function `change_base` that converts a given number to a specified base. It also includes unit tests to ensure the correctness of the function. The `test_change_base` function contains a series of test cases to verify the functionality of the `change_base` function.