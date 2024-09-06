```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The function returns `True` if any of these conditions are true, and `False` otherwise. 

Here is a test drive code to test the functionality of the function:
```python
test_cases = [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (0, 1, 1, True),
    (-1, 2, -1, True),
    (2, -3, 6, True),
]

for x, y, z, expected in test_cases:
    actual = any_int(x, y, z)
    assert actual == expected, f"Expected {expected} for ({x}, {y}, {z}), but got {actual}"
```

The above code loops through each test case and asserts the expected output against the actual output from the `any_int` function.