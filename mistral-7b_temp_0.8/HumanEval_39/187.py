

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
    from collections import deque
    n = int(n)
    if n < 2:
        return n
    q = deque(maxlen=n)
    q.append(2)
    q.append(3)
    f = 5
    while len(q) < n:
        f = f + 2
        for c in q:
            if not (f % c):
                break
        else:
            q.append(f)
    return q[-1]

