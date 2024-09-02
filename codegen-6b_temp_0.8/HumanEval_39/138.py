

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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        first_number = 1
        second_number = 1
        number = first_number + second_number
        while number < n:
            first_number = second_number
            second_number = number
            number = first_number + second_number
        return number

