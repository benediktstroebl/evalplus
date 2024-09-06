```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of their unit digits. The unit digit is the digit in the ones place of a number, which is retrieved by indexing the string representation of the number `-1` with the negative indexing syntax `[-1]`. 

This is exemplified in the test cases provided, and the function returns the expected output based on the unit digits of the input numbers, taking into account the sign of the product, as per the last example in the prompt.