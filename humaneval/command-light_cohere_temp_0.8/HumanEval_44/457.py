```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of integer x to base base and returns string representation.
    """
    Example a function must work with integer input and any valid base number.

    Parameters:
    x (required to be an integer), 
    base (required to be an integer and cannot be zero)
    """
    assert base != 0, "Base cannot be zero"
    assert isinstance(x, int), "Input should be an integer"
    return _change_base(x, base)

def _change_base(x, base):
    # Apply the conversion
    # Use string formatting to ensure base format
    return f"{x:>{base}")

# Test cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(7, 2), '111')
assertEqual(change_base(-5, 10), '500')
assertEqual(change_base(0, 20), '20')
assertEqual(change_base(123, 5), '_/\N')
assertEqual(change_base(-123, 2), '-_ \N')
```
The function `change_base` takes two parameters, `x` and `base`, representing the number to be converted and the base number, respectively. The function first asserts that `base` is not zero, as a valid base cannot be zero. Then, it calls `_change_base` helper function, which performs the actual conversion using the conversion formula `x^\alpha = x` with `\alpha` raised to the base. 

Finally, the function returns the converted string representation of `x` in the desired base. 

These test cases ensure that the function works correctly for different scenarios, including non-integer inputs, non-positive bases, and negative numbers.