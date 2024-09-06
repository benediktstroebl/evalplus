```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of both numbers. The unit digit is the last digit of a number. This is achieved by using the built-in function `str` to convert both input integers to strings, accessing the last digit of each string using `str(a)[-1]` and `str(b)[-1]`, and then multiplying these extracted digits together using the built-in `int` function. 

Let's test it with some examples:
```python
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))  # Output: 20
```
All examples test correctly against the expected output. Feel free to test it with other sets of numbers as well!