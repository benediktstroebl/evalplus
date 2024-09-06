```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers as input and extracts the unit digits of both numbers by accessing the last digits of their string representations with `int(str(a)[-1])` and `int(str(b)[-1])`. It then multiplies these unit digits and returns the resulting integer. 

Here is an example usage of the function:
```python
print(multiply(12, 3))
```
This would print:
```
36
```

This is because the unit digits of 12 and 3 are respectively 2 and 3, and 2 * 3 = 6 = 36. 

This implementation ensures that the function is self-contained and does not rely on any external variables or assumptions. 

It also adheres to the problem statement by returning the product of the unit digits, even if the input integers have zero or negative values. 

This solution is streamlined and minimally complex.