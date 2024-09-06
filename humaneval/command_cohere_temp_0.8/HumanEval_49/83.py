```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n % p` by leveraging the built-in function `pow(x, y, p)`, which works for positive integers `x`, `y`, and `p` and returns `x` raised to the power of `y` modulo `p`. This is a powerful tool for modular arithmetic calculations. 

The tests would be run against the function to check its correctness. These tests ensure the function's behavior against various inputs. Would you like me to provide these test cases or continue with another task?