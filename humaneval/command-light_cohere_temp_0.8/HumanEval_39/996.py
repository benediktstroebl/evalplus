Here is a self-contained Python function that solves the given problem:
```python
def prime_fib(n):
    """
    Returns the n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    is_prime = True  
    # checks whether a number is prime using the sieve ofEratosthenes method
    for i in range(2, n+1):
        is_prime &= (not sieve_of_Eratosthenes[i])
    return next((i for i in range(2, n+1) if is_prime), None)
```

This function will return the n-th Fibonacci number that is prime, where n is the input to the function. It uses a simple approach of iterating over numbers from 2 to n and using the sieve of Eratosthenes method to check whether each number is prime or not.