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
This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. The function employs a basic primality tests, starting with checks for divisibility by 2 and 3, and then uses a loop to continue checking larger primes up to the square root of the input number.