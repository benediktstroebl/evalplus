

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
    # I don't know how to solve this one with less than O(n)
    fib_list = [2, 3]
    p_fib_list = [2, 3]

    i = 2

    while len(fib_list) < n:
        fib_list.append(fib_list[i-1] + fib_list[i-2])

        # Because we start with fib[2], fib[1] is prime
        if i >= 2:
            p_fib_list.append(fib_list[i-1] + fib_list[i-2])

        for j in range(2, p_fib_list[-1] + 1):
            if p_fib_list[-1] % j == 0:
                break
        else:
            p_fib_list.append(p_fib_list[-1])

        i += 1

    return p_fib_list[n - 1]

