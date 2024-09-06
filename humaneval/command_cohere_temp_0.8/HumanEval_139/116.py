Here's a Python script that defines the `brazilian_factorial` function as per the provided description:
```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```

This script provides a function called `special_factorial` that accepts an integer `n` as input and returns the special factorial for that integer, as defined in the problem statement. The function operates by multiplying all integer values from 1 to `n` together to obtain the result.