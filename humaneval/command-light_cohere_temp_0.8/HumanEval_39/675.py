```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    Returns None if n < 0.
    """
   
    def is_prime(num:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    """
    if n == 0:
        return None
    a, b = 2, 3
    for i in range(2, n + 1):
        if is_prime(a):
            a, b = b, a + b
        else:
            break
    return b
```