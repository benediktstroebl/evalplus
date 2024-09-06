

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
    if n < 2:
        raise ValueError("n must be greater than 1")
    
    fib_list = [0, 1]
    current_num = 0
    while current_num < n:
        if n % current_num == 0:
            raise ValueError("This is not a prime number")
        current_num = fib_list[-1]
        fib_list.append(current_num)
    
    return fib_list[-1]

