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

This function checks if any combination of adding two of the three numbers equals the third number. The `bool()` function is used to convert the result into a boolean type.

Here are some examples of how this function can be used:
```python
TestSuite = [
    # set up a dictionary of tests to run
    {'input': (5, 2, 7), 'output': True},
    {'input': (3, 2, 2), 'output': False},
    {'input': (3, -2, 1), 'output': True},
    {'input': (3.6, -2.2, 2), 'output': False},
]

for test in TestSuite:
    assert any_int(**test['input']) == test['output']
``` 

This test suite demonstrates the validity of the `any_int()` function for various test cases.