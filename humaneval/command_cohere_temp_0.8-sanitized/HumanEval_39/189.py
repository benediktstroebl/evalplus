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
    Generates the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Here we try to use recursion, but if it exceeds max recursion depth,
    # it switches to iteration mode.
    def fib_helper(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        rec_res = prime_fib(n - 1) + prime_fib(n - 2)
        if is_prime(rec_res):
            return rec_res
        return fib_helper(n - 1)
    
    if n > 2 and is_prime(fib_helper(n)):
        return fib_helper(n)
    
    # If the above recursion isn't prime and n > 2, then we're sure
    # that the answer must lie within the range [2, n] (exclusive).
    # We therefore iterate and test each number in this range.
    for num in range(2, n + 1):
        if is_prime(num) and num != n - 1:
            return num
    
    return None