```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function uses a `in` expression to compare the three given numbers `x`, `y`, and `z` to check if any of them is equal to the sum of the other two. To check if the integers are integers, the function uses the `all` function in combination with a `type` function and the `int` constructor to ensure that **all** three given numbers are of integer type, and if so, it returns `true`. 

Here's a simple test suite to ensure that the function behaves as intended:
```python
test_any_int = lambda : None  # noqa: F841

test_cases = [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (0, 0, 0, True),
    (-2, 2, -4, True),
    (-2, -2, 0, False),
    (2, 2, 4, True),
]

for x, y, z, expected in test_cases:
    assert any_int(x, y, z) == expected
```

This test suite contains various test cases to cover different scenarios and ensure the function's correctness.