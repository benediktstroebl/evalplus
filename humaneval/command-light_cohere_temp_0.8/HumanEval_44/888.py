```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    Return string representation after conversion.
    base numbers less 10."""
    return '{:b}'.format(x, base)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(12, 4) == '24'
    assert change_base(7, 5) == '111'
    assert change_base(3, 10) == '30'
    assert change_base(0, 2) == '20'
    assert change_base(1, 1) == '20'

# Example usage
test_change_base()
```
This Python script defines a function `change_base` that converts a given number `x` to a specified base `base`. The function returns the converted string representation. 

The `test_change_base` function contains assertions to validate the correctness of the `change_base` function. These assertions check they different scenarios and ensure the function's expected behavior. 

The example usage demonstrates how to call the `change_base` function with different inputs and bases, and it provides the expected string representation after the conversion.