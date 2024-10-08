Here is a self-contained Python script that defines a function is_prime that checks whether a given number is a prime or not, and passes the tests you have provided:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
This function is_prime takes an integer n as input and checks whether it is a prime number or not. It uses some basic heur conditions to determine if a number is prime, and the tests you have provided align with those conditions.