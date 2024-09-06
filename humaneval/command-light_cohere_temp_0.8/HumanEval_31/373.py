Here is a self-contained Python script that solves the problem of determining whether a given number is a prime, and passes the tests provided:
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
This script defines a function called `is_prime` that checks whether a given number `n` is prime or not. The function uses a prime factorization technique, starting with the assumption that all primes greater than 2 are of the form 6n + 1, where n is a positive integer. 
The function then checks for divisibility by 2 and 3, and if the number is divisible by either of these, it returns `False`. If the number is not divisible by 2 or 3, the function then checks for divisibility by numbers of the form 5i + 2, where i is an integer. The function then continues this process by incrementing i by 6, and repeats until i is less than the square root of the number. 
This process effectively eliminates the potential for divisors smaller than the square root of the number.