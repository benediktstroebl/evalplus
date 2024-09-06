```python
from itertools import count, takewhile

def is_prime(n):
    """
    is_prime checks if number is prime
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    if n < 2:
        return False
    for i in count(2):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    # We use the formula of Fibonacci numbers to deduce that each Fibonacci number after the first two is F[n] = F[n-1] + F[n-2].
    # When we encounter a number that is prime we store it in the list primes and thereafter continue the loop.
    # When nth turn arrives we return the last prime Fibonacci number before n.
    primes = []
    fib_gen = (fibonacci_seq for fibonacci_seq in takewhile(
        lambda x: x[0] < 2e4, ((1, 1), (1, 0))
    ))
    for fib in fib_gen:
        n1, n2 = fib
        if is_prime(n1) or is_prime(n2):
            primes.append(n1)
            primes.append(n2)
        if len(primes) == n:
            return primes.pop()
```

## Explanation:
1. The `is_prime` function is a simple primality test that checks if n is less than 2 or if n has any divisors besides 1 and itself. This is a basic implementation of the [Eratosthenes' sieve](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) algorithm.
2. The `prime_fib` function starts by checking if `n` is less than 1, and if so, raises a `ValueError` as the `prime_fib` function requires a positive integer input.
3. We use the formula for Fibonacci numbers to generate the sequence. The `takewhile` function ensures the loop terminates when the first element of a Fibonacci sequence exceeds 2e4. This is necessary to prevent overflow.
4. For each Fibonacci number generated, we check if it (or its previous number) is prime using the `is_prime` function. If it is prime, we store it in the `primes` list.
5. When the length of `primes` reaches `n`, we return the last prime Fibonacci number before n (since the list is in order) using `primes.pop()`. 

This approach avoids the need for a large matrix of Fibonacci numbers, which would be very large, and instead uses a simple formula to generate the numbers as needed and combines it with a prime checking mechanism to find the n-th prime Fibonacci number efficiently. 
```