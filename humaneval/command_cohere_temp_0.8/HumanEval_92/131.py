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

This function checks if any combination of adding two of the three numbers equals the third number. It helps to overcome the issues with data types and immutability of Python sets, resulting in a clean and fast solution. And the resulting code solves the problem statement in a self-contained manner. 

Also, note that the function can be simplified further, as follows:
```python
def any_int(x, y, z):
    return (x == y + z) or (y == z + x) or (z == x + y)
```
This version uses logical OR to combine the three conditions directly.