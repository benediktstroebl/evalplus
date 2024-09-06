

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
    fib = [1, 1]
    index = 2
    prime = 2
    while index < n:
        if is_prime(fib[index - 1]):
            prime = fib[index - 1]
        fib.append(fib[index - 1] + fib[index - 2])
        if fib[index] > prime:
            while not is_prime(fib[index]):
                fib.pop()
                index -= 1
            index += 1
        else:
            index += 1

    return fib[n - 1]

