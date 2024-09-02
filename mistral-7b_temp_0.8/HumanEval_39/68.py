

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

    fib_sequence = []

    # Starts with 0 and 1
    fib_sequence.append(0)
    fib_sequence.append(1)

    # Finds next numbers in Fibonacci sequence
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    # Checks for each number in the Fibonacci sequence if it's prime
    for i in range(1, len(fib_sequence)):
        if fib_sequence[i] > 1 and is_prime(fib_sequence[i]):
            return fib_sequence[i]
    else:
        return None

