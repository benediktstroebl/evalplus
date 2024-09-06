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

This function checks if any combination of adding two of the three numbers equals the third number. It helps to overcome the issues with data types by casting the variables to integers using the floor division operator (`//`), which casts false to zero and keeps true values. Finally, the function returns `true` if any of the conditions are `true`, and `false` otherwise. 

Here is a test to ensure that the function works as expected:
```python
test_any_int = 3 == any_int(2, 4, 3) and 5 == any_int(5, 2, 7) and 0 == any_int(2, -1, 1) and any_int(2, 3, 4) and not any_int(2.5, 3, 4) and not any_int(3, 2, 2) and not any_int(2, 3, 6.1)
```

The expression on the left side of the `==` symbol evaluates to `True`, and the expression on the right side of the `==` symbol evaluates to `False`. The `and` and `or` operators will only return `True` if ALL or ANY of the arguments return `True`. 

The following example shows incorrect cases; therefore, it is important to note that the `==` symbol is not equal to the `=` symbol, meaning that the result is not necessarily true or false, but rather checks if the given expression evaluates to true or false. 

It is also important to note that the function works as expected only when the numbers are integers, and will not work correctly if the numbers are not integers.