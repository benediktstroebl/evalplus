```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of their unit digits. The unit digit is the digit in the ones place of an integer. This is achieved by using the built-in function `str` to convert both input integers to strings, accessing the last character (the unit digit) using `str(a)[-1]` and `str(b)[-1]`, converting these characters back to integers using `int`, and then multiplying them together. 
This approach directly computes the product of the unit digits, ensuring a valid and efficient solution.

Here is an example of an output of the function:
```
multiply(12, divisible by 5) = 2
```