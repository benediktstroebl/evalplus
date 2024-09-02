

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
    fib_list = [1, 2]
    for i in range(2, n):
        x = fib_list[-1] + fib_list[-2]
        if x >= n:
            break
        else:
            fib_list.append(x)
            if fib_list[-1] > n:
                return fib_list[-1]
            if x % 2 == 0 and x != 2:
                continue
            for k in range(3, int(x**0.5) + 1, 2):
                if x % k == 0:
                    break
            else:
                fib_list.pop()
    return fib_list[-1]

