```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation.
    base numbers are specific to 10
    """
    We convert the input to a string and perform base-conversion using the `decimal()` function
    """
    return str(decimal(x))

def test_change_base():
    try:
        assert change_base(8, 3) == '22'
        assert change_base(7, 16) == '7c'
        assert change_base(3, 2) == '20'
        assert change_base(10, 10) == '1'
        assert change_base(0, 5) == '0'
        assert change_base(5, 5) == '05'
        assert change_base(-5, 2) == '-20'
        assert change_base(float(2), 10) == '20'
        assert change_base(27, 3) == '82'
    except AssertionError:
        raise
test_change_base()
``` 
The `change_base` function takes an integer `x` and a base `base` as input and returns the string representation of `x` in the specified base. It uses the` decimal `decimal()` function to convert the input to a string, and then applies the appropriate base conversion. 
The `test_change_base` function contains a series of assertions that test the correctness of the `change_base` function. 
When you run this script, it will run the tests and display the output.