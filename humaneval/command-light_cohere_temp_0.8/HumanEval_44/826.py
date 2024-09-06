```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are raw_base is 10
    """
    # we convert the number into a string
    return "{:0b}".format(x, base)

def test_change_base():
    #test case 1
    assert change_base(8, 3) == '22'
    #test case 2
    assert change_base(5, 2) == '100'
    #test case 3
    assert change_base(7, 2) == '111'
    #test case 4
    assert change_base(35, 10) == '350'
    #test case 5
    assert change_base(34, 15) == '68'
```
The function `change_base` takes an integer `x` and an integer `base` as input and returns a string representation of `x` in the specified base. 
This function uses the built-in function `{:0b}`.format() from the Python string module to perform the conversion.