```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the digit in the ones place of a number, the far right of any number. This is achieved through the use of the built-in function `str` to convert both input numbers to strings, and then using `int` to convert only the last digits (the unit digits) back to integers for multiplication.

Here is a test drive code to test the function:
```python
def test_multiply():
    # Test case 1
    assert multiply(148, 412) == 16, "Failed test case 1"

    # Test case 2
    assert multiply(19, 28) == 72, "Failed test case 2"

    # Test case 3
    assert multiply(2020, 1851) == 0, "Failed test case 3"

    # Test case 4
    assert multiply(14, -15) == 20, "Failed test case 4"

test_multiply()
```

The test drive code will ensure the functionality of the `multiply()` function works appropriately. 

*Note*: Please let me know if you would like any adjustments to the script or if you want to tackle any other coding problem! I'm happy to help.