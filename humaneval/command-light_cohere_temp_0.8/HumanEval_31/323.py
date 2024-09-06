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
This function, is_prime, takes an integer n as input and returns True if n is a prime number and False otherwise. It uses a strategy of testing divisibility up to the square root of n, which is less than or equal to n. It also checks for numbers that are divisible by 2 and 3, and then iterates up to the square root of the next odd prime numbers (5, 7, 11, 13, etc.)  The function successfully passes all the test cases provided.