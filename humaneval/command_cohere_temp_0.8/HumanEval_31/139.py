```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
``` 

This function defines a recursive function `is_prime` that returns `True` if the number is prime, and `False` otherwise. It checks if the number is less than 2, which would make it not prime, and if the number is divisible by any number from 2 to `n` divisors, which would make it not prime as well.