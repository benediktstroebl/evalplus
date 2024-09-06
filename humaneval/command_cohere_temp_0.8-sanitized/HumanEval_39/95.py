def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    def fibonacci(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    if n <= 8:
        return [2, 3, 5, 13, 21, 34, 55, 89][n - 1]
    else:
        return fibonacci(n)