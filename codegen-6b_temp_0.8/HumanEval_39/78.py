

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
    fib_n = []
    index = 2
    fib_n.append(2)
    while len(fib_n) < n:
        fib_n.append(fib_n[index-1] + fib_n[index-2])
        index += 1
    for i in range(len(fib_n)):
        if is_prime(fib_n[i]) == True:
            if fib_n[i] == n:
                return fib_n[i]
        else:
            fib_n.remove(fib_n[i])
