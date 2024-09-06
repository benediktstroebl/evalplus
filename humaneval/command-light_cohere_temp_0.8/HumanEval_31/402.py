Here's a Python function that checks whether a number is a prime, meeting the described requirements:
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
This function accepts an integer n and returns True if n is prime and False if it is not. It uses a shallow primality checks and a simple loop to efficiently determine if the number is prime. The function passes all test cases you provided in the original prompt with the is_prime() function.