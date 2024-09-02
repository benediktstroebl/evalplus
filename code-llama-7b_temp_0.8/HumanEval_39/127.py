

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
    # check that the input is correct
    if n <= 0:
        raise ValueError(f'n must be positive. Got: {n}')

    # the output value
    output = None

    # a counter for the number of iterations
    i = 0

    # try to find a prime fibonacci number
    while output is None:

        # increase the counter
        i += 1

        # check if the current Fibonacci number is prime
        if is_prime(fibonacci(i)):

            # stop the iteration when the target is reached
            if i == n:
                output = fibonacci(i)

    # return the result
    return output

