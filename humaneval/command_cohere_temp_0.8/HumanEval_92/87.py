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

This function checks if any combination of adding two of the three numbers equals the third number. It works with the principle that if `x == y + z` is true, at least one of `a` or `b` is `1`, making the entire expression `a || b || c` true.

Here is a simple test suite that can be used to validate the function:
```python
# Tests:
test_cases = [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (0, 1, 2, True),
    (-1, 2, 3, True),
    (5, -10, -5, True),
]

for x, y, z, expected in test_cases:
    assert any_int(x, y, z) == expected
```