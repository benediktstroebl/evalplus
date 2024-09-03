```python
def is_simple_power(x, n):
    if n == x or n == 0:
        return True
    elif x % n == 0:
        return False
    else:
        return True
```

This function takes two arguments - x and n, where x is the number being tested for simplicity, and n is the exponent. It uses the simple algorithm to test if x is a simple power of n, which involves checking if n is equal to x or 0, and if so, it returns True. If x is not a simple power of n, or n is not equal to 0, it returns False.