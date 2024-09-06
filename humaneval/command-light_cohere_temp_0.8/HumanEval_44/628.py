```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base B"""
    # convert integer to string
    s = str(x)
    # check if string has digits
    if '.' not str(s) != '':
        return s
    else:
        return s.if we need to recalculate the digits to have the same length,
        # we add a 0 to the beginning of the number and
        # convert the rest to decimal representation
        return '{0}' + str(x)

# test case
print(change_base(8, 3))
print(change_base(7, 2))
``` 
This code defines a function `change_base` that takes two parameters: `x` and `base`. It converts the base of `x` to base `base` and returns the string representation of the result.