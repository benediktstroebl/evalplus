```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the digit at the far right of a number or the digit that is not multiplied by any other digits. The function uses the `-1` indexing offset to retrieve the last digit of each number, converts it to an integer using `int()`, and then multiplies them together. 

Let's validate the functionality with some examples for which the answer is known:
```python
print(multiply(148, 412))  # Should print 16
print(multiply(19, 28))  # Should print 72
print(multiply(2020, 1851))  # Should print 0
print(multiply(14, -15))  # Should print 20
```
The function passes all the test cases and computes the desired product from the unit positions of the entered integers.