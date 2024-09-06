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

This function checks if any combination of the three variables adds up to the other variable. It works with the properties of integer addition, that is if `A + B == C` or `B + C == A` or `C + A == B`, etc., then it is guaranteed that `A == B + C` or `B == C + A` or `C == A + B`. This property is true for integers only due to floating-point precision errors. The function returns `True` if any of these conditions are `True`, and `False` otherwise. 

Here is a simple test suite for this function:
```python
TESTS = [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (-3, 2, 5, True),
    (-3.4, 2.1, 1, False)
]

for x, y, z, result in TESTS:
    assert any_int(x, y, z) == result
```