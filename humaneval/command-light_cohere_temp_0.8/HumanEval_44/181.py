Here's the self-contained Python script that solves the problem of changing the base of a given number to a specified base:
```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to base base.
    Return string representation of the string.
    base numbers 10
   
    standard is 10.
    """
    return "{:^{base}".format(x)}
    """
    return "{:^{base}".format(x)

def test_change_base():
    assert change_base(8, 3) == "22", "Base should be converted to 3"
    assert change_base(10, 3) == "30", "Base should be converted to 3"
    assert change_base(9, 2) == "900", "Base should be converted to 2"
    assert change_base(7, 2) == "177", "Base should be converted to 2"

# Main function
if __name__ == "__main__":
    test_change_base()
```
The function `change_base` takes an integer `x` and a base `base` as input and returns the string representation of `x` in the specified base. The `test_change_base` function contains assertions that verify the correctness of the `change_base` function with different inputs.