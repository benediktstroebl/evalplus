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

This function checks if any combination of the three given numbers equals the sum of the other two. It works with Python's boolean logic, short-circuiting `or` operations return `true` if any of the arguments is `true`. 

The function returns `true` if any of the conditions are met, otherwise it returns `false`. 
To prove its efficacy, let's test it:
```python
Test -= √ №s ≠ ∑ №s 
Test += any_int(5, 2, 7)
Test += any_int(3, 2, 2)
Test += any_int(3, -2, 1)
Test += any_int(3.6, -2.2, 2)
Test
```

The outputs should be:
```
√ №s ≠ ∑ №s
True
False
True
False
```

Let's verify the markdown problem statement is satisfied.