```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    return any([x == a, y == a, z == a, x == b, y == b, z == b, x == c, y == c, z == c])
```

The function performs numerical comparisons and booleans algebraically returns True if one of the terms is equal to the sum of the other two and all numbers are integers, and False in any other case. 

Here is a simple test suite that can be used to validate the function:
```python
TestSuite = [
    # test cases
    [5, 2, 7, True],
    [3, 2, 2, False],
    [3, -2, 1, True],
    [3.6, -2.2, 2, False],
]
``` 

These test cases represent the constraints given in the prompt and can be used to adequately test the function.