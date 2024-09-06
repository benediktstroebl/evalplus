```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This script defines a Python function called `special_factorial` taking a single argument `n`, representing the integer for which we want to calculate the 'special factorial'. This function then proceeds to calculate the 'special factorial' by iterating through all numbers from 1 to `n` and multiplying them together. This multiplication process mimics the mathematical definition of the 'factorial' function, which is denoted by `n!` and represents the product of all integers from 1 to `n`. The result of this computation is the 'special factorial' of `n`, which would be the outcome of the function.

This solution is concise and straightforward, directly implementing the mathematical definition of the 'factorial' function to calculate the 'special factorial' in a clear and effective manner.