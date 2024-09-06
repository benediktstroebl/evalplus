```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    """ returns the difference string representation.
    base numbers are this might 10
    """
    conversion is based on the fact that 10^n is 
    the nth digit of n in base b.
    Convert it to string format
    """
    return '{:02}'.format(x).
    """
    return '{:02'.format(x)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(7, 2) == '111'
    assert change_base(1, 10) == '1'
    assert change_base(10, 10) == '10'
    assert change_base(10, 2) == '2010'
    assert change_base(0, 100) == '0'
    assert change_base(0, 1) == '0'

# Start the execution of the main function.
# Run the test function to check the correctness of the change_base function.
test_change_base()
```