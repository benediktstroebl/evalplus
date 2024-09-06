```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This function checks if a given number is prime, using a simple algorithm that also handles the edge cases. It will return `True` if the number is prime, and `False` otherwise. 

It is a self-contained function with tests passed through the function.