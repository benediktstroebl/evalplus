

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
    x = [1,2]
    a = 0; b = 1; count = 1
    while count != n:
        c = a + b
        a = b
        b = c
        x.append(c)
        count += 1
    f = False
    for num in x:
        if num == 1:
            f = True
            continue
        if is_prime(num):
            if f: return num
    if not f: return False
