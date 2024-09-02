

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

    # check if the number is prime
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        fib_number = fibonacci(n)
        prime_number = is_prime(fib_number)
        if prime_number == True:
            return prime_number
        else:
            return prime_fib(n-1)
