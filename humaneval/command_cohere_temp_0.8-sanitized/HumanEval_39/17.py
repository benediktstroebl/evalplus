def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    else:
        pmf = [2, 3]
        for i in range(2, n):
            pmf.append(pmf[i-1] + pmf[i-2])
        for i in range(2, len(pmf)):
            if is_prime(pmf[i]):
                return pmf[i]