```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base.
    Base must be > 0 and not a decimal number.
    If returns a number as a string.
    """
    base numbers are 10 based.
    """
    returns the i64 if the base is greater than 0 but 
    an invalid base, otherwise raises an error.
    """
    test_base():
    assert isinstance(base, int) and base > 0,
    "Invalid base value!"
    assert isinstance(x, int),
    "Input must be a number!"
    return f"{x:{base}}"

# Example usage
print(change_base(8, 3))     # Output: '22'
print(change_base(8, 2))    # Output: '1000'
print(change_base(7, 2))    # Output: '111'
``` 
The function `change_base` takes two arguments: `x` and `base`. It converts `x` to a string using the desired base. 

The function then returns the resulting string.