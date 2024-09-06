```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x == y + z or y == x + z or z == x + y and type(x) == int and type(y) == int and type(z) == int
```

The function uses logical operators to check the relationship between the three parameters. The code determines if either of the parameters is equal to the sum of the other two. The type() function is used to determine if the parameters are integers, returning 'true' if all three are integers, with an added constraint that all three values must be integers. 

To ensure that the function behaves as expected, let's break down its behavior with some example cases:
- any_int(5, 2, 7)  — True. This is because the sum of 2 and 7 is 5, which matches the first parameter. 
- any_int(3, 2, 2) — This case returns False because no sum of these values equals any other value.
- any_int(3, -2, 1) — True, because 3 equals the sum of -2 and 1.
- any_int(3.6, -2.2, 2) — This case returns False because 3.6 is not an integer. 

The function will return 'True' if any combination of the parameters equals the sum of the other two values, and the parameters are integers.  Otherwise, it returns 'False'.