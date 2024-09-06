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
This code defines a function named is_prime that checks whether a given number n is prime or not. The function first handles special cases where n is less than or equal to 1, as these numbers are not prime. It then checks for divisibility by 2 and 3, returning False if either of these numbers are divisible by n. 

It then enters a loop that iterates up to the square root of n, checking for divisibility by consecutive odd numbers (i+2). Finally, it returns True if no such of these divisors were found during the loop.