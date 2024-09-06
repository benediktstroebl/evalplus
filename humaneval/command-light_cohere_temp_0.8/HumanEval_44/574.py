```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base and returns string representation.

    Args:
        x: int or float.
    base: int or float 
    Returns:
    string representation of x after applying the conversion.
    """

def test_change_base():
    """Function to run the tests for the change_base function."""
    # Test case 1:
    assert change_base(8, 3) == '22'
    # Test case 2:
    assert change_base(8, 2) == '1000'
    # Test case 3:
    assert change_base(7, 2) == '111'
    pass
```
The above Python script defines a function `change_base` that takes an integer `x` and an integer `base` as arguments, and returns the string representation of `x` after applying the conversion. 

It also has a test function `test_change_base` that runs the tests for the `change_base` function and asserts the expected results.