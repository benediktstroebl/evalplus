

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
    result = 0
    if n == 0:
        result = 2
    elif n == 1:
        result = 3
    else:
        fibs = fib()
        primes = prime()
        counter = 0
        for x in fibs:
            if counter == n:
                result = x
                break
            else:
                if is_prime(x):
                    counter += 1
    return result
