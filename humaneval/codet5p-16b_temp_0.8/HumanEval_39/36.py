

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

    pre = [2, 3]
    num = pre[-1] + pre[-2]
    while len(pre)!= n:
        divisors = [x for x in range(2, num) if num % x == 0]
        if len(divisors) == 0:
            pre.append(num)
        num += pre[-1] + pre[-2]
    return num
