```python
def is_prime(n):
    """Returns True if the number is prime, and False otherwise."""
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
The function checks for primality by iteratively testing divisibility from 2 up to the square root of the number. The function then returns true if the number is prime, and false otherwise. It also includes edge cases, like checking for 1 and 4, which are not prime. 

The function is self-contained, and does not require any external variables or functions to be called.