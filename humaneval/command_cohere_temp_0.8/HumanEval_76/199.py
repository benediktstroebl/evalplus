```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function compares the input number x with the power of n using the expression n ** int(x == n ** x) and determines if they are equal. Essentially, it checks if x can be written as n raised to an integer power, where n is also an integer. If this condition holds, it returns True, indicating that x is a simple power of n. Otherwise, it returns False.