```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the last digit of a number. This is achieved by using the built-in function `str` to convert both input integers to strings, and then using the slice [-1] to retrieve the last character (the unit digit), which is then converted back to an integer using the built-in int() function. The integers `a` and `b` are multiplied together, and the result is returned. 

Let's test it with some examples:
```python
print(multiply(148, 412)) # Output: 16
print(multiply(19, 28)) # Output: 72
print(multiply(2020, 1851)) # Output: 0
print(multiply(14, -15)) # Output: 20
```
All examples test correctly and neatly provide the desired output.