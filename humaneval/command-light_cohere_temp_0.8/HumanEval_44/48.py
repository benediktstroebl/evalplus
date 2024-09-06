```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    Return string representation after conversion.
    """
    base numbers less than 10
    >>> change_base(8, 3) # Should return '22'
    """
    if base not in [2, 10]:
        raise ValueError("base should be 2 or 10")
    return "{:0>1d}".format(x, base)

def test_change_base():
    try:
        x = 8
        result = change_base(x, 10)
        assert result == '8'
        result = change_base(x, 2)
        assert result == '100'
    except AssertionError as e:
        print(f"Failed assertion: {e}")
        assert False
    return result

# Example usage
test_change_base()
 ``` 
This code provides a function `change_base` that converts a number to a specified base, and tests the function using the `test_change_base` function. The tests assert the expected outputs for given inputs.