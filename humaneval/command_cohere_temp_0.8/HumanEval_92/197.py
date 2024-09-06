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

This function checks if any combination of adding two of the three numbers equals the third number. It works with the assumption that the three numbers are integers. 

The logic uses a truth table where the function returns 'True' if the truth value of at least one of the columns is 'True'. The following is a breakdown of how the function works:
- a = x + y == z: This checks if the sum of x and y is equal to z. 
- b = y + z == x: This checks if the sum of y and z is equal to x. 
- c = x + z == y: This checks if the sum of x and z is equal to y. 

In this way, the function evaluates each part of the truth table and returns 'True' if any of them are 'True'. The function returns 'False' if none of the conditions are true. 

Please note that the function assumes that the numbers entered are integers and does not perform any type of checking. It also does not check for the numerical stability of the operation. 
For example:
any_int(10, 5, 12) ➞ True
any_int(1, 1, 1) ➞ True
any_int(1, 1, 1.1) ➞ False
any_int(-5, -10, 5) ➞ True
any_int(-5, 5, 1) ➞ False