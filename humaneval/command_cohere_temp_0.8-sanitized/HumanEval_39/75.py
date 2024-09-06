def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Starts with larger prime Fibonacci numbers
        num = 10 ** (n - 2).bit_length()
        return prime_fib(num)[0]