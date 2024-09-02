

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
    number = 1
    is_fibo = False
    while not is_fibo:
        number = get_fibonacci_number(number)
        if is_prime(number):
            is_fibo = True
    return number

