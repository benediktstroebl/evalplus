

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
    if n < 0:
        return "Invalid"

    # if n is already Fibonacci, return the number
    if fibonacci(n):
        return n

    # value fibonacci[n] is a Fibonacci Number, and it's also a prime number
    fibonacci_list = generate_fibonacci_list(n)
    for num in fibonacci_list:
        if not is_prime(num):
            return num

