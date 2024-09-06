```python
def multiply(a, b):
    """Returns the product of the unit digits of the input integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of the unit digits of `a` and `b`. The unit digit is the last digit of an integer when it is written in base 10. This is achieved through the use of the built-in function `str` to convert both inputs `a` and `b` to strings, and then through the use of the slice notation `[-1]` to retrieve the last character (which is always a digit), converting it back to an integer using the `int` function. 

Here's an example usage of the function:
```python
print(multiply(12, 4))
```
This will print out the result "3" to the console, as the unit digits of 12 and 4 are respectively 1 and 4, and 1 * 4 = 4 ==> 3.