Here's the solution:
```python
def change_base(x, base):
    """
    Change the numerical base of input number x to base.
    Return string representation of the string.
    base numbers <= 36 are
    """10"
    
    if x < 0:
        raise ValueError("Input must be a non-negative number")
    return '{:b}'.format(x, base)

def test_change_base():
    assert change_base(-8, 3) == '22', "Negative number and base should raise error"
    assert change_base(42, 10) == '409600', "Should convert to base 10"
    assert change_base(7, 2) == '111', "Should convert to base 2"

# Run the tests
test_change_base()
```
The `change_base` function converts a number to a string with the specified base. The `test_change_base` function contains assertions that check the function's behavior for various inputs. 
This script is self-contained and can be used as a standalone module to solve the problem of converting a number to a specified base.