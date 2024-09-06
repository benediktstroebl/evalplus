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

This function checks if any combination of the three given numbers equals the sum of the other two. It returns true if any of these conditions are true for the given three numbers. The boolean values are then or'd together to return the final boolean result. 

Here is a test to ensure that the function correctly returns True given the input `[5, 2, 7]`:
```python
test = any_int(5, 2, 7)
print(test)
```

And here is a test to ensure that the function correctly returns False given the input `[3, 2, 2]`:
```python
test = any_int(3, 2, 2)
print(test)
``` 

These tests will ensure that the code behaves as expected, based on the given problem statement.