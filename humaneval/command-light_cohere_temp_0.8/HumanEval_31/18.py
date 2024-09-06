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
This Python function checks if a given number is prime or not. It uses the simple and efficient algorithms to determine primality. The function then handles numbers up to `n` (inclusive) as input and returns `True` if the number is prime, and `False` otherwise. 

The function uses a "6k" test to efficiently identify prime numbers up to the square root of the number.