```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts their unit digits (the last digit of each number) using string manipulation, and then returns the product of these unit digits. This is accomplished by using `int(str(a)[-1])` and `int(str(b)[-1])` to isolate the last digits of each number, performing the multiplication, and then returning the result.