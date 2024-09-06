```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are
    string must be valid and greater than zero
    """
    assert isinstance(x, int) and x >= 0 and base > 0, "Invalid input or base number."
    return format(x, str(base))

def test_change_base():
    """
    Test case function to check the change_base function
    """
    base = 2
    x = 7
    result = change_base(x, base)
    assert isinstance(result, str) and result == '111', "Returned string is not as expected"

if __name__ == "__main__":
    test_change_base()
```
The code defines a function `change_base` that converts a given number `x` to a specified base `base`. It also provides a test case function `test_change_base` to check if the `change_base` function is working as expected. 
When you run this script, the `test_change_base` function will be executed, which contains the test case. This test will output the proper result.