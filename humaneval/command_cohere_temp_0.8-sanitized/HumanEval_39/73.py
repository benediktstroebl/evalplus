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
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # This list stores the ( Fibonacci number, Next Fibonacci Number )
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    # This list stores the indices of the fibonacci numbers that are prime
    prime_fib_indices = [i for i, val in enumerate(fib) if is_prime(val)]
    return fib[prime_fib_indices[n - 1]]