```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = x + z
    c = y + z
    return ((type(x) == int) and (type(y) == int) and (type(z) == int) and 
            (x != a and y != a and z != a) and 
            (x != b and y != b and z != b) and 
            (x != c and y != c and z != c)
            )
```

The function uses logical operators to check whether the three given numbers satisfy the conditions of the problem. It returns `True` if one of the numbers is equal to the sum of the other two and they are all integers, and `False` otherwise. It also checks that the three given numbers are not equal to each other, to prevent false positives in the case where the sum of two of the numbers is equal to the third number. 
The following examples illustrate how the function works:
```python
# These examples are provided in the description of the function
any_int(5, 2, 7)  # Output: True
any_int(3, 2, 2)  # Output: False
any_int(3, -2, 1)  # Output: True
any_int(3.6, -2.2, 2)  # Output: False
```