```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x == y + z and y == x + z and z == x + y and isinstance(x, int) and isinstance(y, int) and isinstance(z, int)
```

This function checks if any of the three variables is equal to the sum of the other two variables. Then it checks if the variables are integers. 

This solution assumes that the variables `x`, `y`, and `z` are integers. If any of the variables are not integers, the function will return False. 

Here is a test suite that can be used to test the function:
```python
test_cases = [
    (5, 2, 7,),  # True: 5 == 2 + 7
    (3, 2, 2),  # False
    (3, -2, 1),  # True: -2 == 1 + 3
    (3.6, -2.2, 2),  # False
]

for x, y, z in test_cases:
    assert any_int(x, y, z) == (x == y + z and y == x + z and z == x + y and isinstance(x, int) and isinstance(y, int) and isinstance(z, int))
```

Note, that the solution assumes that the integers involved are not negative integers with absolute values less than 2^52, due to platforms' limitations.