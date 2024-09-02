

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
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    def is_prime(num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for fib_num in fib_numbers:
        if is_prime(fib_num):
            return fib_num

