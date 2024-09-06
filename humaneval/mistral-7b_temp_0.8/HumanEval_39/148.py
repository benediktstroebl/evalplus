

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
        raise ValueError("n must be a positive integer")

    fib_list = [1, 2]
    fib_num = 2
    while fib_list[-1] < n:
        fib_num = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_num)
        if any(fib_num % i == 0 for i in range(2, fib_num)):
            fib_list.pop()
            continue
        is_prime = True
        for i in range(2, int(fib_num ** 0.5) + 1):
            if fib_num % i == 0:
                is_prime = False
                break
        if is_prime:
            break

    return fib_num
