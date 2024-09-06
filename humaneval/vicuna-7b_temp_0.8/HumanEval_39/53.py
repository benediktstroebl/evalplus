

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # 2 is the first Fibonacci number and it's the first prime number
    # (notice that 0! = 1)
    if n == 2:
        return 2
    
    # we know that the n-th Fibonacci number starts with 1, so we can compute the first two numbers
    # and then use the recurrence relation to get the n-th number
    fib_num = 1
    n_num = 1
    for i in range(2, n):
        fib_num, n_num = (fib_num * (i + 1), n_num * i)
    
    # we have the two numbers, now we need to check if they are prime
    if n_num % 1:
        return n_num
    if fib_num % 2:
        return fib_num
    for i in range(3, int(n**0.5) + 1):
        if fib_num % i:
            return fib_num
    return None
