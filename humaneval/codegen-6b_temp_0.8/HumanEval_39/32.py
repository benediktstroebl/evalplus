

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
    if n <= 1:
        return n
    is_prime = [True for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i**2, n+1, i):
                is_prime[j] = False
    result = 1
    for i in range(n):
        if is_prime[i]:
            result = result + i
    return result

