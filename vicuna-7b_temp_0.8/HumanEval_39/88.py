

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
    # if n <= 3
    if n <= 3:
        return n
    # else
    else:
        # calculate the previous two numbers
        a, b = fibonacci(n-1)
        # check if the number is prime
        if n % 2 == 0:
            return a
        else:
            for i in range(a, b + 1):
                if i % 2 == 0:
                    return 0
            return 1
