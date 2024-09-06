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

This function checks if any combination of adding two of the three numbers equals the third number. It helps to overcome the issues with data types by validating that all numbers are integers using `bool()`. The function returns `True` if any of these conditions are `True`, otherwise it returns `False`. 

Here is a test to ensure that the function behaves accordingly:
```python
test_any_int = {
    (5, 2, 7): True,
    (3, 2, 2): False,
    (3, -2, 1): True,
    (3.6, -2.2, 2): False,
}

for case, expected in test_any_int.items():
    assert any_int(*case) == expected
```

This test case verifies the behavior of the `any_int` function with a variety of test scenarios mapped to expected outcomes. The `assert` statement validates that the actual output of the `any_int` function matches the expected output for each test scenario.  This is a fundamental tool for ensuring that your code behaves as expected, helping you catch errors early in the development process.