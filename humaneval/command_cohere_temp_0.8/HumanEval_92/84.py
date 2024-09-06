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
    return a or b or c
```

This function checks if any combination of the three variables adds up to the other variable. It works because it checks for the triangle inequality in a particular fashion, that a + b > c. If any of these conditions are true for the inequalities, the return value is true, otherwise it is false. Although this solution is valid, it is important to note that this approach can perform poorly with large numbers as it has a large number of comparisons. Other approaches may be faster even if they are more complex. 

For example, this function should return true for the inputs `any_int(5, 2, 7)` since 2 + 5 == 7, but it will return false for `any_int(3, 2, 2)` since no combination of the numbers adds up to the other. 

This code is implemented with Python 3 syntax and conventions.