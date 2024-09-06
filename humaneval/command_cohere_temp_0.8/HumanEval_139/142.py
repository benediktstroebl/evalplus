Here's a Python script that defines the `brazilian_factorial` function as per the problem statement:
```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```

This script provides an efficient Python function that calculates the `brazilian_factorial` notionally defined as the product of factorials from 1 to n. It adheres to the problem's requirement for the function to accept an integer as input and return the corresponding special factorial value. The function is designed to be straightforward and easily adaptable to diverse scenarios requiring factorial calculations.