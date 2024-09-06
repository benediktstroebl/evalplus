def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_prev = 2
    prev = 3
    fib_num = 5
    
    while fib_num <= n:
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        fib_num = prev + prev_prev
        prev_prev = prev
        prev = fib_num
    
    return None