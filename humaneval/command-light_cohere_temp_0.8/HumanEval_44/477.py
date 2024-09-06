```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of input number x to base base.
    return string representation after conversion
   
    base numbers less than 36 are converted directly, 
    while others are rounded to the nearest integer.
    """
    return str(x, base)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(7, 16) == '17'
    assert change_base(123, 2) == '2000'
    assert change_base(0, 4) == '0'
```  The above function `change_base` accepts two parameters: `x` which is the number to be converted and `base` which is the base to convert it to. but the function converts the string representation of the input number `x` using the specified `base`. It then returns the string representation. 

The `test_change_base()` function acts as a test case for the `change_base` function and checks that the function returns the correct result for the given input.