Here is a Python script that demonstrates how to determine whether a given number is a prime number:
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
This function is_prime takes a number n as input and returns True if n is a prime number and False if it is not.

This function uses a combination of basic primality checks and the fact that all prime numbers greater than 3 are of the form 6k + 2k(k is odd) where k is less than √5. It also uses an trial method to efficiently find all the prime factors of a given number.

The function is then tested with a series of numbers, and the results are printed to the console.