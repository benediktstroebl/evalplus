```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and is a prime.
    Assumes that n is a positive integer.
    Returns: number in the mathematical sequence that begins: 1, 1, 2, 3, 5, ...
    """
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
            if is_prime(a):
                return a

def is_prime(n: int):
    """
    Check whether n is prime or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
```