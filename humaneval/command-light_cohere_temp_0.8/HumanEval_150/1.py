Here's a self-contained Python script that solves the problem of determining whether a given number is prime or not, using a simple recursive approach:
```python
def is_prime(n):
    """Check if n is prime"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
This function, `is_prime`, takes a number `n` as input and checks if it's prime or not using a simple recursive approach. The function returns `True` if `n` is a prime number and `False` otherwise. 

This approach uses basic trial and error to determine primality, and has a time complexity of O(sqrt(n)), which is the time it would take to factorize a given number.