```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.
    Returns False if it's not prime.
    """
    generates a random prime numbers using the Sieve of Eratosthenes
    """
    sieve = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        sieve[i] = False
    fib = 1
    while len(sieve) > 0:
        if sieve[fib] == False:
            break
        fib += 1
    return fib
```