Here's a self-contained Python function to determine if a number is prime or not:
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
This function, named **'is_prime'**, checks whether a given number is prime or not. It employs a specific conditions to determine prime numbers and returns 'True' if the number is prime, and 'False' otherwise.