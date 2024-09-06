from itertools import count, takewhile
def is_prime(n):
    """
    Determines whether n is prime
    """
    if n <= 1:
        return False
    for i in count(2):
        if n % i == 0:
            return False
    return True
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Keep incrementing Fibonacci numbers until we find n primes consecutively
    count = 0
    num = 0
    while True:
        # 2nd Fibonacci number is 1, so start from 3
        next_num = 3 if num == 1 else int(num**0.5 + num)
        num, count = takewhile(lambda x: is_prime(x), count, next_num)
        if count == n:
            return num