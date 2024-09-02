

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

    counter = 1
    last_two = [1, 1]
    prime_number = 2
    while counter < n:
        last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
        if last_two[1] % prime_number == 0:
            counter += 1
    return last_two[1]

