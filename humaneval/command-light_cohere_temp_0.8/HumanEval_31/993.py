Here is a Python script that defines a function is_prime that checks if a given number is a prime number, and passes all your tests:
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

This function is_prime takes an integer n as input and returns True if n is a prime number, and False otherwise. It uses the checking various divisibility conditions up to a square root of n, and finally returns True if all these conditions are satisfied.