```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers use 10
    exact numbers
    """
    return '{:g}'.format(x, base)
    """
    return "{:g}" if x <= base else "{:.2g}".format(x, base)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(5, 2) == '100'
    assert change_base(7, 4) == '000111'
    assert change_base(0, 101) == '1'
    assert change_base(9, 2) == '20'
    assert change_base(10, 5) == '05'
    assert change_base(5, 10) == '50'
    assert change_base(1, 1000) == '10100'

# Call the function and test
test_change_base()
```
This script defines a function `change_base` that converts a given number `x` to a base `base` using string formatting. The `test_change_base` function contains several assertions to test the correctness of the `change_base` function with different inputs and base numbers.

Finally, the `test_change_base` function is called to validate the correctness of the function.