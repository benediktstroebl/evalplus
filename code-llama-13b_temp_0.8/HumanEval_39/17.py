

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
    primes = []
    fib_numbers = []
    n_1 = 1
    n_2 = 1
    fib_numbers.append(n_1)
    fib_numbers.append(n_2)

    for i in range(2, 200000):
        n_th = n_1 + n_2
        n_1 = n_2
        n_2 = n_th
        fib_numbers.append(n_th)

    # Checking if fibonacci numbers are prime.
    for number in fib_numbers:
        is_prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
        if is_prime:
            primes.append(number)

    # Checking if prime fibonacci numbers are consecutive
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 1:
            continue
        else:
            break
    return primes[i + 1]

