```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by accessing the last index of their string representations using `str(a)[-1]` and `str(b)[-1]`. These last digits are multiplied using `int()` to ensure the result is also an integer. The function returns the resulting product. 

Here is an example usage of the function:
```python
print(multiply(12, 4))
```
This would print:
```
12
```

This indicates that the last digit of the product 12*4 is 12. 

This function solves the given problem in a straightforward manner and produces the desired outcome.