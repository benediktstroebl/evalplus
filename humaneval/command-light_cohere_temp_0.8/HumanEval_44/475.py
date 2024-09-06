```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    >>> return f' decimal representation using base conversion rules
    """
    if x < 0:
        raise ValueError("Input cannot be negative.")
    return f"{x:.{{base}"

def test_change_base():
    """Function to test the change_base function"""
    assert change_base(-5, 10) == "-5.0"
   
    result = "base10 conversion of -5 failed."
    assert change_base(10, 10) == "10.0"
    result = "base10 conversion of 10 failed."
    assert change_base(15, 2) == "111"
    assert change_base(7, 5) == "227"
    assert change_base(123, 1) == "123"
    assert change_base(0, 0) == "0"
    assert change_base(3, 20) == "333"
    assert change_base(27, 40) == "1333"
    assert change_base(7, 700) == "000393"

# driver code
print("Results:",end)
print(test_change_base())
``` 
This script defines the function `change_base` which converts a given number to a specified base. It also includes a test function `test_change_base` that contains a variety of tests that verify the correctness of the `change_base` function.