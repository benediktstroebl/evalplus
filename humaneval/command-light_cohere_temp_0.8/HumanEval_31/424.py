Here's a self-contained Python function that checks whether a given number is a prime or not:
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
This function implements a trial-and-error based primality test that checks divisibility by consecutive odd numbers up to the square root of the number. It then returns True if the isn't divisible by any such prime, and is therefore prime.