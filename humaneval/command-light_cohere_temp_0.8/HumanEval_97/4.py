```python
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume that test is valid."""
    if type(a) != int or type(b) != int:
        raise TypeError("Both inputs must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive")

    return sum([int(num) for num in str(a).format(10))] * sum([int(num) for num in str(b).format(10)])
```
This script defines a function called `multiply` that takes two integers as input and returns the product of their unit digits. The function performs input validation to ensure that both inputs are integers and that they are positive.