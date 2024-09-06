Here is a self-contained Python script that defines a function is_prime that checks whether a given number is a prime number or not:
```python
def is_prime(n):
    """Returns True if the number is prime, False otherwise."""
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

This function is_prime takes an integer n as input and checks whether it is a prime number using the trial division method combined with some basic conditions. It returns True if the'd number is prime, and False otherwise.