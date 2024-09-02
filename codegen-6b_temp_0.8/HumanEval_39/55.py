

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
    result = None
    # we know that there are n-1 Fibonacci numbers
    # The sum of the last two Fibonacci numbers is the nth Fibonacci number
    fib_n = [1, 1]
    while len(fib_n) < n:
        sum_n = fib_n[-1] + fib_n[-2]
        fib_n.append(sum_n)
    for num in fib_n:
        if is_prime(num):
            result = num
            break
    return result

