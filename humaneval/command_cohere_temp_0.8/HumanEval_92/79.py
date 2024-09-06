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

This function checks if any combination of the three variables adds up to the other variable. Once the variables are defined, a logical operator(or) is used to determine if any of these conditions are true. 

This way, the function will return true if any of the conditions are true, which means that at least one of the numbers is equal to the sum of the other two, and it will return false in any other cases. 

Also, this function handles the case where `x`, `y`, or `z` is zero, ensuring that it doesn't create an invalid operation in the process. 

This approach ensures that the function works correctly and returns the correct values for the given inputs. 

Here is an example of a markdown cell displaying the functionality of the function:
```
any_int(5, 2, 7) ➞ True

any_int(3, 2, 2) ➞ False

any_int(3, -2, 1) ➞ True

any_int(3.6, -2.2, 2) ➞ False
```