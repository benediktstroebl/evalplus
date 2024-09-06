

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
    fib_numbers = [1, 2]
    fib_numbers[1] = fib_numbers[0] + fib_numbers[1]

    for i in range(2, n):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

    for i in range(len(fib_numbers)):
        is_prime = True
        for j in range(2, fib_numbers[i]):
            if fib_numbers[i] % j == 0:
                is_prime = False
        if is_prime:
            return fib_numbers[i]

