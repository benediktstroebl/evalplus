

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

    # Initialize
    fib = [0, 1]
    prime_fib = 0

    # Loop until we get prime fibonacci number
    while prime_fib == 0:
        # Add fibonacci
        fib.append(fib[-1] + fib[-2])

        # Check if it's prime
        prime_fib = 1
        for i in range(2, int(fib[-1]/2)+1):
            if fib[-1] % i == 0:
                prime_fib = 0
                break

    return fib[n-1]

