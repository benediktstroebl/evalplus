

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

    def is_prime(n: int):
        if n < 2:
            return False
        i = 2
        while i**2 <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    
    def gen_fib(n: int):
        previous_prev = 1
        previous = 2
        while n > 0:
            yield previous
            temp = previous
            previous = previous_prev + previous
            previous_prev = temp
            n -= 1
    
    fib_gen = gen_fib(n)
    for i, val in enumerate(fib_gen):
        if i == n - 2 and is_prime(val):
            return val
