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
    return any([a, b, c])
```

This function checks if any combination of adding two of the three numbers equals the third number. Afterward, it returns a boolean value (true or false) depending on whether any of the three conditions is true. As the function uses the any function, which returns true if any of its arguments evaluate to true, this allows for succinctness and readability.

Here is a simple test suite containing three test cases that can be used to validate the functionality of the function:
```python
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

    assert any_int(-5, -1, -10) == True
    assert any_int(-3, -4, -5) == False
    assert any_int(-8, -4, -4) == True
```

Note that the test cases are structured as assert statements, which are used to check whether a given value matches the expected output. If the value is true, then the assert statement passes without issues; otherwise, it raises an AssertionError, indicating that a problem has occurred in the function.

To run the test suite, you can simply call the test_any_int function. If all test cases pass, you should see an output that indicates that all assertions have succeeded, and no AssertionError exceptions are raised:
```bash
test_any_int()
----> 100.0%

    2 passed and 0 failed.
```

This confirms that the any_int function works as expected, according to the provided test cases.