Here is a Python function that checks whether a given number is a prime or not, it utilizes the Sieve of Eratosthenes algorithm to efficiently determine prime numbers:
```python
def is_prime(n):
    if n <= 1:
        return False
    pi = 3
    while pi * pi <= n:
        if n % pi == 0:
            return False
        pi += 2
    return True
```

This function takes an integer `n` as input and quickly verifies if it is a prime number using the Sieve of Eratosthenes algorithm. The function runs in O(n) time complexity, which is an efficient method for finding prime numbers.