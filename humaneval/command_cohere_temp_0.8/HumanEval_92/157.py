```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = y + z
    c = x + z
    
    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False
```

The function conducts three successive additions to compare the target numbers to the sum of the other two. It then checks if the sum is an integer and if any of the checks yield a match. The result is a boolean reflecting these comparisons. 

This problem can also be solved with `any()` and `all()` functions combined in a more concise way, but the response example is not meant for that approach.