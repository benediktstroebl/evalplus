

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
        previous_number = 5
        current_number = 13
        for _ in range(3, n):
            previous_number, current_number = current_number, current_number+previous_number
            if not (current_number % 2) and (current_number % 5):
                continue
            else:
                return current_number

