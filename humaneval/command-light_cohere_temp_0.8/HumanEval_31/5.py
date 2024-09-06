```python
def is_prime(n):
    """
    A function that checks whether a number is prime or not.

    Args:
        n (int): Number to check.

    Returns: boolean value, true if the number is prime, false otherwise.
    """
    Print(f"Is {n} prime?
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