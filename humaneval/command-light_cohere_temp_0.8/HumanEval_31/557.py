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
This code defines a function called is_prime that takes an integer n as input and returns True if n is a prime number and False otherwise. The function uses a specific logic to check for primality, such as testing divisibility up to the square root of the number and only returning True for prime numbers. 

This function is self-contained and can be used to determine whether a given number is prime or not, passing any test for primality.