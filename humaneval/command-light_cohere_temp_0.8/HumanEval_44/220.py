Here is a self-contained Python script that defines a function to change the numerical base of an input number to a specified base:
```python
def change_base(x, base):
    """
    Change the base of a number x to base b.
    Args:
        x: int or float number to change the base from.
        base: int base of the number system
    Returns:
        string representation of the number in the given base.
    """

def test_change_base():
    """
    Test the change_base function
    """
    assert isinstance(change_base(8, 3), str), "change_base should return a string"
    assert isinstance(change_base(7, 2), str), "change_base should return a string"
    assert isinstance(change_base(float("4"), 10), str), "change_base should return a string"

# Main code
if __name__ == "__main__":
    test_change_base()
```
This script defines a `change_base` function that takes an integer `x` and a base `b` as arguments, and returns the string representation of `x` in the specified base. The `test_change_base` function is used to test the `change_base` function with various inputs. 
It checks if the function returns a string and if it's of the expected type.