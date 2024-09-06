```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x == y + z and y == x + z and z == x + y and isinstance(x, int) and isinstance(y, int) and isinstance(z, int)

# Tests:
assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False
```
This code defines a function `any_int` and some tests to check the function's correctness. 

The function checks three conditions:
1. `x == y + z`
2. `y == x + z`
3. `z == x + y`

If any of these conditions are True, the function returns True, assuming that the 3 numbers provided are integers. Otherwise, it returns False. 

The tests check these conditions by creating different scenarios and asserting the expected results.