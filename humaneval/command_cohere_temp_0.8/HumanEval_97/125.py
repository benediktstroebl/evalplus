```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The code uses the last character extraction using `str(a)[-1]` and `str(b)[-1]` to obtain the unit digit of the respective numbers, and then using an integer multiplier returns the product of these unit digits. 

The function can take any valid input, as specified in the problem statement, and will return the corresponding product of the unit digits.  This approach leverages direct integer multiplication to compute the solution.  This is a basic but effective approach to the problem.