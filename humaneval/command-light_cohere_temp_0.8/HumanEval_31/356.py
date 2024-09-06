Here is a Python script that defines a self-contained function is_prime to determine if a given number is a prime, and it passes all the tests:
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
This function, `is_prime`, determines whether a given number `n` is prime or not. It uses a specific rules and testing approaches to quickly identify prime numbers and determine if the number is prime or not.

The function first determines if `n` is less than or equal to 1, in which case it returns `False` since primes don't have 0 or 1. It then verifies whether `n` is 2 or 3, returning `True` since these are prime numbers.

Next, it performs a loop starting from 5 and checks if `n` is divisible by any power of `i` or `i + 2`, where `i` is increased by 6 each iteration. If any such, it returns `False` since these are divisors of prime numbers.

Finally, if none of these conditions are met, the function returns `True`, indicating that `n` is a prime number.

This function can be used to quickly determine whether a given number is prime or not, which is useful for various applications involving prime numbers and number theory.