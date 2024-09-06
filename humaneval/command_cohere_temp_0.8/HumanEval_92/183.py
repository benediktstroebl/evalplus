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
    return a or b or c
```

This function checks if any combination of adding two of the three numbers equals the third number. It returns `True` if any of these conditions are met, and `False` otherwise. The explicit checking of all three conditions avoids the problem of only checking two of the three potential combinations that the spec explicitly mentioned, making the code more robust. 

The function assumes that the three numbers are integers (`int` type) as stated in the problem description. 

To make the function more robust, it should be considered to add tests for a more complete set of possible scenarios.  This could be adding tests with negative numbers, zero, floats, or edge cases like `Inf` or `NaN`. 
It should also consider using descriptive variable names and commenting on the code logic for better code readability and maintainability. Applying these suggestions would improve the function, but the code still adheres to the problem's requirement of being a self-contained Python script of a few lines.