

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
    f_n = [0, 1]
    for i in range(2, n):
        f_n.append(f_n[i - 1] + f_n[i - 2])
    for i in range(len(f_n) - 1, -1, -1):
        if f_n[i] <= 2:
            f_n.pop()
        else:
            break
    for i in range(len(f_n)):
        if all(f_n[i] % j != 0 for j in range(2, f_n[i])):
            return f_n[i]

