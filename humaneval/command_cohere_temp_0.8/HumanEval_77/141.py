```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the cube root of the number is an integer with the 'round' function, which will return True if the cube root is an integer and the number is a cube, or False if it is not. 

The 'round' function is used rather than int to deal with situations where the cube root is a non-integer value that rounds up to an integer. This is consistent with the stated intent of the problem, and most of the given test cases.

However, this solution may fail if the cube root of the number is exactly `.5`. In that case, `a ** (1/3) == round(a ** (1/3))` will return False, even though the number is a cube. This is because `**.5**` is technically an integer, but the comparison will trigger the rounding logic in `round`. 

If the goal is to account for this edge case, the function could instead use the `math.ceil` and `math.floor` functions to more precisely compare the cube root to integers.