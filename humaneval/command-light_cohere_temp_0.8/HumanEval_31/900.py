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
This code defines a function `is_prime` that checks whether a given number `n` is prime or not. It employs various algorithms to determine primality, such as checking divisibility by 2 and 3, and then checking divisibility by numbers within the range [5, i] The function returns `True` if the given number is prime and `False` otherwise. 
This script demonstrates the problem of determining prime numbers in a self-contained manner.