

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
    fib = [0, 1]
    fib_num = 1
    while fib_num < n:
        fib.append(fib[-2] + fib[-1])
        fib_num = len(fib)
        if fib[0] == 1:
            fib.remove(1)
        for i in range(2, int(len(fib)**0.5)+1):
            if fib[len(fib)-1] % i == 0:
                fib.remove(fib[len(fib)-1])
                break
    return fib[len(fib)-1]
