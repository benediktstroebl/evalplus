```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. It works with Python's boolean logic, avoiding the use of explicit `if` statements and thereby reducing lines of code and making the code more readable.

This problem can also be solved in only one line:
```python
def any_int(x, y, z):
    return (x == y + z) or (y == x + z) or (z == x + z)
```

However, such a solution is much less readable and fails to illustrate the logic behind the problem solution. Thus, although the one-liner is shorter, the previous solution is a better option, in terms of utility and understanding.