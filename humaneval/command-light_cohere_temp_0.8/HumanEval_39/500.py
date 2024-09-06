```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and is also a prime.
    return a Fibonacci(n) is a number that is the sum of two preceding Fibonacci numbers: 13(1) + 8(2) = 13, 
    9(3) + 5(4) = 25, ...
    To check whether it's prime, check the factors, none of which are the primes. 
    Factors of 25: 1, 5 
    25 is not prime, so return False 
    """
    if n <= 1:
        return n
    factors = [1, 5]
    for _ in range(2, int(n**0.5) + 1):
        if n % _(factors[-1]) == 0:
            return False
    return n
```