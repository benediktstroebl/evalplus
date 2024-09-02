

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

    fib_numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    number = fib_numbers[n - 1]
    while True:
        if number in fib_numbers:
            fib_numbers.append(number)
            number += fib_numbers[-2]
            continue
        if number > 1000:
            return number
        else:
            return number

