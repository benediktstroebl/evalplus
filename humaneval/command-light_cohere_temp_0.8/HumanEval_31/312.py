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
This function checks if a given number is prime, and returns True if it is prime and False otherwise. It uses a test-time algorithm, which checks divisibility with the squares of consecutive numbers starting from 5, and uses the concept of divisibility by 2 and 3 to reduce the number of checks needed.