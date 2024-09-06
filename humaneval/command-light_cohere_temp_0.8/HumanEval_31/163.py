Here is a self-contained Python script that checks whether a given number is prime or not:

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

This function checks whether a given number is prime or not. It uses the simple algorithm that checks divisibility of numbers up to the square root of the number, with a few extra checks for oddities. The function returns True if the numbers passes all tests, and False otherwise.

You can use this function to test whether different numbers are prime or not.