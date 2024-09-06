```python
def is_prime(n):
    """Returns true if the number is prime, and false otherwise."""
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
This code defines a function is_prime that checks if a given number n is a prime number. The function returns True if the is prime and False otherwise. The function uses some heuristic that iterates through the numbers 2 to the square root of n, and checks if n is divisible by any of them. The function performs well and passes the tests with the test cases.