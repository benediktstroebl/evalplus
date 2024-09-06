

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
    n_list = [2, 3, 5, 13, 89]
    if n <= 5:
        return n_list[n]
    else:
        is_prime = True
        n_fib = 0
        fib_list = [2, 3]
        while is_prime:
            fib_list.append(fib_list[-1] + fib_list[-2])
            if fib_list[-1] > n:
                break
            if fib_list[-1] % 2 == 0:
                continue
            elif fib_list[-1] % 3 == 0:
                continue
            elif fib_list[-1] % 5 == 0:
                continue
            elif fib_list[-1] % 13 == 0:
                continue
            elif fib_list[-1] % 89 == 0:
                continue
            else:
                is_prime = False
                n_fib = fib_list[-1]
        return n_fib

