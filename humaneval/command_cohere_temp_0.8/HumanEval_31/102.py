```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and satisfies the given tests, returning true for prime numbers and false for non-prime numbers. You can use it to determine whether a number is prime or not. 

You can continue to iterate and improve your understanding of prime number determination techniques, such as the `Sieve of Eratosthenes` or the `Miller Rabin` test, to name a few, which are efficient ways to test primality in various scenarios.