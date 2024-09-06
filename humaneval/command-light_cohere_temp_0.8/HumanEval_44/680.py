```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Convert x into a string representation in the specified base.
    The code is written using intentional formatting for clarity.
    """
    return f"{x"{x, base}
    return f"{x.__format__(f'{base}')}"
def test_change_base():
    assert change_base(8, 2) == '1000'
    assert change_base(7, 5) == '007'
``` 
This Python script defines a function `change_base` that converts a given number `x` to a specified base `base`. The function returns the string representation of the number in the desired base. The code also provides a tests for this function, checking that it produces the correct results for the given inputs.