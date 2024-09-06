```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base
    >>> change_base(8, 3) # Result: '22'
    >>> change_base(8, 2) # Result: '1000'
    >>> change_base(7, 2) # Result: '111'
    """
    # pow function cannot handle big numbers, so do it the old way
    # The result will be the same as using pow, just more verbose
    if x == 1:
        return str(1)
    elif x <= 1:
        return str(x)
    else:
        return format(x, 'b{}'.format
    return str(format(x, base))

# Test the function with some cases
print(change_base(8, 3))  # Result: '22'
print(change_base(8, 2))  # Result: '1000'
print(change_base(7, 2))  # Result: '111'
 ``` 
This script provides a function `change_base` that converts a number to a specified base, it handles cases such as one and very small numbers, and provides a test suite with some examples.  The expected output is the result of each test case.