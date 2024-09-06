```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number. It does so by taking the difference between the input number and the largest integer less than or equal to the input number, as represented by the expression `int(number)`. This effectively captures the fractional part of the number and returns it as the output. 

This function directly solves the challenge statement, providing a straightforward way to capture and return the decimal component of a floating-point number. 

To validate the behavior of the function, you can run some tests like this:
```python
# Test case
assert truncate_number(3.5) == 0.5

# Edge case
assert truncate_number(3.) == 0.
assert truncate_number(2.) == 0.
``` 

These tests confirm that the function behaves as expected, in line with the problem statement. 

This approach showcases a simple and direct solution to the problem, nicely demonstrating the elegance and utility of the Python language.