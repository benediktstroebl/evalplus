Here's the solution:
```Python
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
This function checks if a number is prime by trying to divide it by numbers starting from 2 and 3, then 5, increasing the threshold by 6 each time until the number is not divisible by any integer less than or equal to the square of the threshold.