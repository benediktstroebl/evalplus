

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

    def is_prime(number: int):
        if number == 2:
            return True
        if number < 2 or number % 2 == 0:
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    def prime_fib_number(index: int):
        if index == 1:
            return 2
        if index == 2:
            return 3
        else:
            a, b = 2, 3
            for _ in range(index - 2):
                a, b = b, a + b
            return b

    i = 1
    number = prime_fib_number(i)
    while not is_prime(number):
        i += 1
        number = prime_fib_number(i)

    return number

