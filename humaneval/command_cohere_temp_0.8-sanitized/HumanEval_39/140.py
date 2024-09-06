def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer.")
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    for _ in range(n - 2):
        if is_prime(fib[_]):
            return fib[_]
        # Since fibonacci numbers are very dense among primes,
        # we can skip verifications for fibonacci numbers which are not prime.
        if not is_prime(fib[_] - 1) and not is_prime(fib[_] - 2):
            return fib[_]
    # We reached the last possible number, so we picked the last one.
    return fib[-1]