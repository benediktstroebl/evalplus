

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
    fib_terms = [1, 1]
    new_fib_terms = [1, 1]
    while True:
        fib_terms[0] = fib_terms[1]
        fib_terms[1] = new_fib_terms[0] + new_fib_terms[1]
        if is_prime(fib_terms[1]):
            if fib_terms[1] > n:
                return fib_terms[1]
            else:
                new_fib_terms[0], new_fib_terms[1] = fib_terms[0], fib_terms[1]
