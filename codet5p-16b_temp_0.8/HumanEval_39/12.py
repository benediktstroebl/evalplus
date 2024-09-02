

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

    n_1 = 2
    n_2 = 3
    counter = 1

    while counter!= n:
        prime_flag = True
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3

        for i in range(2, n_3 // 2 + 1):
            if n_3 % i == 0:
                prime_flag = False
                break

        if prime_flag:
            counter += 1
    return n_3

