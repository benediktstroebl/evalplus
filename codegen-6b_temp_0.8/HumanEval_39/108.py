

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
    fib_numbers = [1, 1]
    for i in range(n-2):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    # If it's even it's always prime
    if fib_numbers[-1] % 2 == 0:
        return 2
    # If it's odd, check if it's prime
    is_prime = True
    for i in range(3, len(fib_numbers)):
        if fib_numbers[i] % 2 == 0:
            is_prime = False
            break

    if is_prime:
        return fib_numbers
    else:
        return 2

