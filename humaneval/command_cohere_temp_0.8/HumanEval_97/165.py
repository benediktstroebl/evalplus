```python
def multiply(a, b):
    """Returns the product of the unit digits of the input integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of the unit digits of `a` and `b`. The unit digit is the last digit of an integer. This is achieved by using the built-in function `str` to convert both `a` and `b` to strings, and then using the slicing operation `str(a)[-1]` to extract the last digit of each integer. The extracted digits are then multiplied using the built-in `int` function, which returns an integer result of the multiplication. 

Here is an example of the function's usage:
```python
print(multiply(12, 4))
```
This would print a result of 4, as the last digits of 12 and 4 are respectively 2 and 4, and 2 * 4 = 4. 

This approach is concise and elegant, bypassing the need for complex conversions and validating the input. It demonstrates the versatility of Python's built-in functions and insights into data manipulation.