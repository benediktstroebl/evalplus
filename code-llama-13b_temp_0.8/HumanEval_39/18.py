

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
    if n < 1:
        raise ValueError("There is no zeroth prime number")
    fib = [0, 1]
    prime = [2, 3, 5, 7]
    index = 4
    while index <= n:
        fib.append(fib[index - 1] + fib[index - 2])
        if check_prime(fib[index]):
            prime.append(fib[index])
            index += 1
        else:
            index += 1
    return prime[-1]

