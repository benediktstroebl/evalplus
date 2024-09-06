

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
    last = 1
    prev = 2
    curr = 3
    while curr < n:
        if is_prime(curr) and is_fib(curr):
            curr = 1
            last = 1
            prev = 2
            curr = 3
        else:
            if is_prime(prev):
                if not is_prime(curr):
                    curr = 1
                    last = 1
                    prev = 2
                    curr = 3
                else:
                    last = prev
                    prev = curr
                    curr += last + prev
            else:
                prev = curr
                curr += last + prev
    return curr
