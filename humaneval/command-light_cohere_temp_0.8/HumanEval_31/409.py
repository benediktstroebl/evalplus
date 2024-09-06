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
This Python function `is_prime` determines whether a given number `n` is prime or not. It employs basic primality testing and some advanced heuricity tests, such as checking divisibility by 2 and 3 and looking for consecutive primes.  This critical part of the implementation is that it doesn't rely on any external functions or data. It can be used to determine whether any given number is prime or not.