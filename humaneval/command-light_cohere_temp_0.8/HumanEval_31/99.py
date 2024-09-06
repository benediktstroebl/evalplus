```python
def is_prime(n):
    """Check whether a given number is prime."""
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
This function, `is_prime`, accepts an integer `n` as an argument and determines whether `n` is a prime number. 

It carries out the process by checking for divisibility by 2 and 3, then employing the square root for these numbers, before performing a loop to check if `n` is divisible by any number from 1 to the square root of the previous number, i. The function ultimately returns `True` if `n` is a prime number, and `False` otherwise.