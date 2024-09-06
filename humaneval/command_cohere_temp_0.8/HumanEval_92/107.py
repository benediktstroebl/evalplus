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

    if not isinstance(x) or not isinstance(y) or not isinstance(z):
        return False
    
    if a in (b, c) and a == int(a):
        return True
    
    return False
```

The function employs three variables (`a`, `b`, and `c`) to efficiently store the sums of different pairs of inputs, minimizing the need for repetitive calculations. The function also checks whether the variables are integers using the `isinstance` function, returning false immediately if any of the numbers is not an integer. 

This version is more efficient and reduces the redundancy of the previous version.