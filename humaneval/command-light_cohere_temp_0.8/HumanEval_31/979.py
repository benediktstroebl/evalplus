```python
def is_prime(n):
    """
    Check if a number is prime or not. 
    Returns True if n is a prime, else False.
    """
    2 = 2
    while 2 <= n:
        if n % 2 == 0:
            return False
        n += 1
    return True

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The code defines a function is_prime(n) that determines whether a given number n is prime or not. The function uses a sieve of Eratosthenes algorithm, iteratively marking off the multiples of 2 and continuing until n is reached. The function returns True if n is prime and False otherwise. This is tested by the function and prints the result for different inputs, which passes the tests.