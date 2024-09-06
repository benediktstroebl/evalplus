```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    Returns the entry in the prime_fib if the number is both a Fibonacci number and a prime.
    """
    return n if n <= 2 or 
    else [n == 3 and n == 5] or 
    ((n-1) // 2) + 2 and is_prime(n)

def is_prime(n: int):
    """
    is_prime checks if n is a prime number.
    """
    return n == 2 or  or n > 1 and [n==1 or n==3 or n==5] and
        all([not is_prime(x) for x in range(2, int(n) + 1))])

# Driver code
print(prime_fib(5))
print(is_prime(6))
```