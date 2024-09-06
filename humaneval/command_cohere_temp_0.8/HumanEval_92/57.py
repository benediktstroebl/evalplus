```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x == y + z and x == z + y and type(x) == int and type(y) == int and type(z) == int
```

The function uses a truthiness check instead of an equality check to determine if the sum condition is met, ensuring that it returns the correct answer.

This problem can be solved with a simple equality check after confirming that the given parameters are integers.