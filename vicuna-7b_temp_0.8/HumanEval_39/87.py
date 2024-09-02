

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
    # check if the input n is a prime number
    if not is_prime(n):
        raise ValueError("Input n is not a prime number")

    # if the input n is prime, return it
    if is_prime(n):
        return n

    # if the input n is not prime, return the first non-prime number that is less than n
    for i in range(2, int(n**0.5) + 1):
        if not is_prime(i):
            return i

    # if the input n is not prime and less than 2, it can't be the n-th number that is a Fibonacci number and it's prime
    if n < 2:
        raise ValueError("Input n is less than 2, it can't be the n-th number that is a Fibonacci number and it's prime")

    # if the input n is not prime, find the smallest index i such that n is the i-th Fibonacci number
    i = 0
    while n > fib(i):
        i += 1
    return n