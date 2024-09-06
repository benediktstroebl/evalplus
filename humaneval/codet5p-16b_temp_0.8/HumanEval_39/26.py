

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

    primes = {2, 3, 5}
    fib_numbers = [1, 2]
    while len(fib_numbers) < n:
        current_fib_number = fib_numbers[-1] + fib_numbers[-2]
        current_prime = current_fib_number
        while current_prime not in primes:
            current_prime = next_prime(current_prime)
        fib_numbers.append(current_fib_number)
        primes.add(current_prime)
    return fib_numbers[-1]

