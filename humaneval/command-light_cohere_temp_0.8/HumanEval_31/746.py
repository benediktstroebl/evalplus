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

This script defines a function `is_prime` that determines whether a given number is a prime. 

The function uses several basic tests, such as divisibility by 2 and 3, and then uses a loop to check for primality using higher values of `i`.  This function can be used to quickly check whether a given number is prime or not. 

Note that this implementation assumes that all input numbers are greater than 1, as checking for primality for numbers below 1 would require additional handling.