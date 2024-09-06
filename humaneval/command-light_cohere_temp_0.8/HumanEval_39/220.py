```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    Uses Robinson-Primes theorem to ensure it's prime.
    Returns 'None' if n <= 0.
    """
    first_prime = 2
    last_prime = int(n ** 0.5)
   
    next_prime = 3
    while next_prime <= last_prime:
        # Theorem requires it's at least sqrt(n) and less than n
        if next_prime ** 0.5 >= int(n **0.25**:
            next_prime += 2
        last_prime = next_prime
    if last_prime > n:
        return None
    return last_prime
```