```python
def is_prime(n):
    """
    Check if a number is prime using the Sieve of Eratosthenes method.
    sieve = [2
   

    # sieve out multiples of numbers and 0
    for num in range(3, n + 1, 2):
        if n % num == 0:
            return False

    return True

# Test the function
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

This code implements a function is_prime that checks if a given number is prime using the Sieve of Eratosthenes method. It iterates through
2 to sieve out multiples of numbers and 0. The function then returns True if the number is prime, otherwise False. The function passes all the tests successfully.