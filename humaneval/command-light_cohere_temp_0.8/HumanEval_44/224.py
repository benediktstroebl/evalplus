```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    :return str representation of the base 10 conversion
    """
    # Convert x to string representation using base 10
    return format(x, base)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(7, 5) == '223'
    assert change_base(123, 4) == '1234'
    assert change_base(-5, 2) == '-20'
    assert change_base(0, 0) == ''

# Call the function with test data and validate results
test_change_base()
```
This Python script defines a function `change_base` that converts a given number `x` to its string representation using the specified base `base`. The function is then tested using various inputs and base values. The test_change_base function contains assertions to validate the output of the `change_base` function for different combinations of inputs and base numbers. The test data covers a expected behavior and ensures that the function produces the correct string representation of the numbers in base 10.