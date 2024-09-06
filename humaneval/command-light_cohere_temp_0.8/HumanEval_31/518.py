Here's a Python function that checks whether a given number is prime:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
```

This function returns True if the number is prime, and False otherwise. It uses a modular division to quickly check divisibility up to the square root of the number, which is the point at which most efficient algorithms begin to have trouble.

I hope this is helpful!