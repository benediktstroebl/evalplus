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

The function employs three conditional statements to check the equality of each of the three potential sums against the other two. The function returns true if one of these conditions is met, and false otherwise.

This approach allows for a straightforward evaluation of the problem requirements and delivers a clear result of either 'True' or 'False'.

This code adheres to Python's style guidelines and maintains readability with explicit variable names like `a`, `b`, and `c`. The function's behavior is further clarified by the documentation string at the beginning of the script. 

To ensure the function's correctness, it is advised to test it against different input scenarios.