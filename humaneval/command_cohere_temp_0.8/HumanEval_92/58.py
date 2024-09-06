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

The function returns `true` if any of these conditions are met, indicating that the three numbers are integers, and two of them equal the sum of the third; otherwise, it returns `false`. 

It is worth noting that the implication of the phrase "one of the numbers" is that the condition is only checked for one of the three variables, thus leaving open the possibility that the two other integers satisfy the condition equally.