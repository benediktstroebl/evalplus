```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. 

The following tests verify the functionality of the `any_int` function:
```python
# True case
print(any_int(5, 2, 7))  # True
print(any_int(3, -2, 1))  # True

# False case
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1.2))  # False
```

All test cases verify the function's correctness in determining whether among the three numbers, two of them sum up to the third number.  This is done using a logical or operation on three conditional statements, each checking a different combination of additions.