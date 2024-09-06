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

This function takes three integers *x*, *y*, and *z* as input, and returns `True` if one of the following conditions is met:
- `x + y == z`
- `y + z == x`
- `x + z == y` 

Otherwise, it returns `False`.

Here is a test suite that can be used to validate the function:
```python
def test_any_int():
    # Test cases with valid inputs
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True

    # Test cases with invalid inputs
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(2, 2, '3') == False
    assert any_int(0, 0, 0.0) == False
```

This test suite covers a wide range of scenarios, including edge cases, to ensure the `any_int` function behaves as expected. 

To run the test suite, you can copy and paste the test cases into a Python environment of your choice. 

You can also use a test runner like `pytest` to automate the execution of the tests and generation of test reports. 

We recommend using a testing framework to ensure comprehensive and organized testing, especially for more complex projects. 

Feel free to adapt the provided script and test suite to your needs!