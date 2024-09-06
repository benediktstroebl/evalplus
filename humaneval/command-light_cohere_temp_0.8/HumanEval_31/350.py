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
This function, named is_prime, takes an integer n as input and returns True if n is a prime number and False otherwise. It uses a basic trial to check for prime numbers, including factors up to the square root of the number.

Let me know if you'd like to explore any other ways to solve this problem or discuss additional concepts related to prime numbers!