```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and is also prime.
    >>> print(prime_fib(1))
    2
    is_prime=(n>=1 and (is_fibonacci_prime(n) or is_fibonacci_prime(n-1)))
    fibonacci=[0,1]
    while(fibonacci[fibonacci[0]+fibonacci[1]]<=n):
        fibonacci.append(fibonacci[fibonacci[0]+fibonacci[1]+fibonacci[fibonacci[0]+fibonacci[1]])
    return fibonacci[n]
  ```