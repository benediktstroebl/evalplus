

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

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, ...)
    fib_nums = [1, 1]
    for _ in range(2, n):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    # Returns Fibonacci number and it's also prime
    for num in fib_nums:
        if is_prime(num) and num not in fib_nums[:_]:
            return num

