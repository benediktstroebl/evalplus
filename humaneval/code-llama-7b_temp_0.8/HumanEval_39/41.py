

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

    # a = 2, b = 3
    a, b = 2, 3

    # a, b, n_fib, n_prime are all positive so if
    # n_fib < n_prime then we need to calculate more fib numbers
    while n_fib <= n_prime:
        # calculate the next fibonacci number
        a, b = b, a + b
        n_fib += 1

        # if n_fib > n_prime then a is the n-th Fibonacci number and
        # calculate if it is a prime number
        if n_fib == n_prime:
            if is_prime(a):
                return a
            else:
                break

        # check if the next number is a prime number and if so,
        # then set a to be this prime number and set n_prime
        # to be the next prime number after a
        if is_prime(a):
            n_prime = next_prime(a)

