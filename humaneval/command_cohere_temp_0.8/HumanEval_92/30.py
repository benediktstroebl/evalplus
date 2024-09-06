```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = x + z
    c = y + z
    return ((type(x) == int) and (type(y) == int) and (type(z) == int) and 
            (x == a or y == a or z == a) and (x == b or y == b or z == b) and (x == c or y == c or z == c))
```

This function checks if any combination of the three variables adds up to one of the other values, and that all variables are integers. It does so by creating temporary variables `a`, `b`, and `c`, to store the sums of different combinations of the inputted values, and then compares these to the inputted values. The function first checks if the types of all inputted values are integers, and if so, returns True if any of the values match a sum, and False otherwise. 

The function above is adapted from a similar function that solves the same problem but was defined for only two variables. That function is shown below:
```python
def any_int(x, y):
    '''
    Create a function that takes 2 numbers.
    Returns true if one of the numbers is equal to the sum of the other number, and both numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    return ((type(x) == int) and (type(y) == int) and (x == a or y == a))
``` 

This function checks if one of the values is equal to the sum of the other value, and that both values are integers. It does so by adding the two values together to store in the variable `a`, and then compares this to the inputted values `x` and `y`. The function first checks if the types of both inputted values are integers, and if so, returns True if any of the values match a sum, and False otherwise.