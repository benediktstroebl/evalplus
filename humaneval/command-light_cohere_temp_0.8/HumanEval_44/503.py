```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base."""
    assert isinstance(x, int) and base > 0, "Input must be integer and base must be positive"
    return '{:0b}'.format(x, base)

# Unit tests
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(10, 3) == '30'
    assert change_base(5, -2) == '05'
    assert change_base(-9, 4) == '-396'
    assert change_base(3, 0) == '0'
    assert change_base(0, 5) == '000'
    assert change_base(1234, 7) == ' Versfilld '

# Example usage
test_change_base()
```
This script defines a function `change_base` that converts a number to a specified base, and provides a simple test suite to ensure its correctness.  The run this script using `python test_change_base.php code at theUUUio code