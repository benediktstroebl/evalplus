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
The function is_prime takes an integer n as input and checks whether it's prime or not. It starts by basic primality checks and then uses a while loop to check divisibility up to the square root of the number, using the condition that a number is prime if it doesn't divide evenly by any number less than or equal to the square of that number.