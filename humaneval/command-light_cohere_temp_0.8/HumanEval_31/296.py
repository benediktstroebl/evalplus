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
This function checks for primality using various algorithms, including square and twin numbers, divisibility by 2 and 3, and a basic trial division. The function also includes edge cases for small numbers and returns False if the input is less than or equal to 1, and True otherwise. 

This function is self-contained and can be used to check the primality of any given number.