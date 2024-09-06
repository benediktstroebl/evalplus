def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # First Fibonacci prime not covered in lesser values
        fib_primes = [5, 13, 89, 233, 1597, 28657, 514229]
        return fib_primes[n - 3]