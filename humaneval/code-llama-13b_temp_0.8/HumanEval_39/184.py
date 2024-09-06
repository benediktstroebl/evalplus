

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

    # the first two Fibonacci numbers
    a, b = 0, 1

    # initialize the counter
    count = 0

    # the index of the Fibonacci number to produce
    fib_num = 0

    # generate Fibonacci numbers
    while count <= n:
        # if the number is prime
        if is_prime(a):
            # increment the counter
            count += 1

        # the next Fibonacci number
        fib_num = a + b

        # prepare the next iteration
        a = b
        b = fib_num

    return fib_num

