```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and extracts the last digit using `int(str(a)[-1])` and `int(str(b)[-1])`. The extracted digits are then multiplied and returned. This solution leverages Python's string manipulation capabilities and the implicit concatenation that the operation `*` induces to directly compute the product of the unit digits. 

Here is a test suite that can be used to validate the function:
```python
def test_multiply():
    # Test case 1
    assert multiply(148, 412) == 16, "Expected 16, but got: {}".format(multiply(148, 412))
    
    # Test case 2
    assert multiply(19, 28) == 72, "Expected 72, but got: {}".format(multiply(19, 28))
    
    # Test case 3
    assert multiply(2020, 1851) == 0, "Expected 0, but got: {}".format(multiply(2020, 1851))
    
    # Test case 4
    assert multiply(14, -15) == 20, "Expected 20, but got: {}".format(multiply(14, -15))
    
    # Test case 5
    assert multiply(11, 322) == 2, "Expected 2, but got: {}".format(multiply(11, 322))

test_multiply()
```

To run the test suite, save the code in a `.py` file and execute the file. The output should indicate that all tests have been passed.