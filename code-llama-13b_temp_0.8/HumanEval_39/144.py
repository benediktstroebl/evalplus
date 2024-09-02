

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
    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        if n == 2:
            return True
        for d in range(2, n):
            if n % d == 0:
                return False
        return True

    def is_fib(n: int) -> bool:
        sq = n * n
        prev = 1
        curr = 1
        next = 2
        while sq > curr:
            prev = curr
            curr = next
            next = curr + prev
            if next == n:
                return True
        return False

    if n == 0:
        return 0
    p_fib = 0
    curr_fib = 2
    while p_fib < n:
        if is_prime(curr_fib) and is_fib(curr_fib):
            p_fib += 1
        curr_fib = curr_fib + 2
    return curr_fib - 2

