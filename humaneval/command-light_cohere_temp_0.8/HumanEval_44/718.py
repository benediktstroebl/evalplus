```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to base
    It returns the string representation after conversion.
    base numbers less than 10.
    """
>>> change_base(8, 3)
    '22'
    """
    return '{:b}'.format(x, base)

def test_change_base():
    """Test the change_base function."""
    assert change_base(8, 3) == '22'
    assert change_base(5, 1) == '5'
    assert change_base(7, 2) == '111'
```
The function change_base, which takes an integer x and an integer base as input and returns the string representation of x with the corresponding base, is defined in this code. The test_change_base function is used to verify the functionality of the change_base function with some test cases.