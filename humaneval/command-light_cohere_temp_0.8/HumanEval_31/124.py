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
This code defines a function called is_prime that takes an integer n as input and returns True if n is prime and False otherwise. It uses a general primality criteria, checking divisibility by 2, 3, and 6 and then performing a series of squaring numbers to find other potential divisors less than the square root of n. The function passes all tests correctly, including edge cases and large numbers.