

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
    # return n-th Fibonacci number
    fib = fibonacci(n)
    
    # check if n-th Fibonacci number is prime
    if n % fib:
        return n
    
    # check if n-th Fibonacci number is the last prime number
    if fib - 1 == n:
        return fib - 1
    
    # check if n-th Fibonacci number is the first prime number
    if fib == n:
        return fib

    # check if n-th Fibonacci number is the second prime number
    if fib + 1 == n:
        return fib + 1

    # otherwise we are in a loop, check if n-th Fibonacci number is the last prime number
    # in this case, we will return n - fib + 1
    # which is the last prime number
    return n - fib + 1