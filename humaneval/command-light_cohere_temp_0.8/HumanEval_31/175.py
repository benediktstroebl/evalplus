Here's a self-contained Python function that determines whether a given number is prime, and it passes all the tests:
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
This function uses an optimized trial division approach to determine whether a number is prime. The function initially determines whether the prime numbers are less than or equal to three, then determines whether the number is divisible by 2 or 3. If the number is not divisible by these two numbers, it then determines whether the number is divisible by any number from 5 (the next prime number) to the square root of the number being tested. The function then returns True if the number is prime and False if it is not.