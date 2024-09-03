def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        # Calculate Fibonacci numbers using recursive approach
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b