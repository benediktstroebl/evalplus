

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
    if n == 1:
        return 2

    if n == 2:
        return 3

    fib_numbers = [2, 3]
    fib_number = 5

    while True:
        if is_prime(fib_number):
            if n == 0:
                break
            n -= 1

        fib_numbers.append(fib_number)
        fib_number = fib_numbers[-2] + fib_numbers[-1]

    return fib_number

