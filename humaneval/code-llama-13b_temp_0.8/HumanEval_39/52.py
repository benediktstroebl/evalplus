

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

    assert n > 0

    fib_values = [1, 1]
    prime_fib_values = []
    while len(prime_fib_values) <= (n - 1):

        # calculates the next fibonacci number
        fib_values.append(fib_values[len(fib_values) - 1] + fib_values[len(fib_values) - 2])

        # if the current fibonacci number is prime, adds it to the list of prime fibonacci numbers
        if is_prime(fib_values[len(fib_values) - 1]):
            prime_fib_values.append(fib_values[len(fib_values) - 1])

    return prime_fib_values[n - 1]

