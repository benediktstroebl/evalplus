def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    if n < 1:
        return None
    elif n == 1:
        return 2
    else:
        # First Fibonacci prime is 2 (corresponds to Fibonacci number 2)
        FibPrimes = [2]
        # Generate Fibonacci numbers and filter primes
        for i in range(2, n + 2):
            FibNum = FibPrimes[-1] + FibPrimes[-2]
            if FibNum in FibPrimes:
                continue  # To avoid duplicates
            if is_prime(FibNum):
                FibPrimes.append(FibNum)
        # Find and return n-th prime Fibonacci number
        return FibPrimes[n - 1]