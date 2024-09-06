

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

    if n == 0 or n == 1:
        return 2

    prime_table = [True] * (n + 1)
    prime_table[0] = False
    prime_table[1] = False

    p, q = 0, 1
    p_q_sum = 2

    while p_q_sum <= n:
        if prime_table[p_q_sum]:
            p = p_q_sum
            q = p_q_sum + q
            p_q_sum = q
            continue
        p += 1
        if p >= n:
            break

    return p_q_sum

