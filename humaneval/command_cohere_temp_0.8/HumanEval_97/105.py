```python
def multiply(a, b):
    """Returns the product of the unit digits of the input integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and extracts the last digit using `str(a)[-1]` and `str(b)[-1]`. It then multiplies these extracted digits and returns the product as an integer. 

Here is an example usage of the function:
```python
print(multiply(12, 3))
```
This would output:
```
6
```

This reflects the problem statement's expectation that the unit digit of the result of multiplying 12 and 3 is 6.