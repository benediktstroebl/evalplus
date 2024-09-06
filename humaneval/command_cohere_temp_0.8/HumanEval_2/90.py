```python
def truncate_number(number):
    """ Returns the decimal part of the number """
    return number - int(number)
```

To test the function, it can be called with a few different input values to see the output and verify that it matches the expected behavior. Here's an example:
```python
# Testing the truncate_number function
assert truncate_number(3.5) == 0.5
assert truncate_number(12.8) == 0.8
assert truncate_number(0.1) == 0.0
```

The function `truncate_number` takes a single argument, `number`, which is a positive floating point number. It returns the decimal part of the number. This is achieved by subtracting the integer part of the number (obtained by converting the floating point number to an integer) from the original number. The integer part of the number is the largest integer that is less than or equal to the given number. The remaining part, after subtracting the integer part, is the decimal part, which is always less than or equal to 1.

The markdown code block can be added to provide context. The function is self-contained and does not depend on any external variables or modules. It is a standalone function that can be copied and pasted into a Python environment and run directly. 
The tests can also be included to evaluate the behavior of the function and verify its correctness. Giving an example of how the test would look like:
```python
# Testing the truncate_number function
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.8) == 0.8
    assert truncate_number(0.1) == 0.0
    assert truncate_number(100.1001) == 0.001
```