```python
def change_base(x: int, base: int):
    """
    Change the base of the number x to base base.
    if x < 0:
        return '0'
    elif base < 2 or base > 36:
        raise ValueError('Invalid base')
    return '{:0>'.format({x:base})[::-1].translate_digits()2}

def test_change_base():
    """Function to test the change_base function."""
    base = 10
    x = 8

    # Test the function
    result = change_base(x, base)
    assert result == '22'

    base = 2
    x = 1000

    # Test the function
    result = change_base(x, base)
    assert result == '1000'

    base = 3
    x = 7

    # Test the function
    result = change_base(x, base)
    assert result == '111'

if __name__ == "__main__":
    test_change_base()
```
The provided code defines a function `change_base` that converts a given number to a specified base. It also has a test function `test_change_base` to verify the correctness of the `change_base` function. 
The `main` block includes the `test_change_base` function, which tests the `change_base` function with different inputs and base numbers.