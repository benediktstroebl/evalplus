

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

    def isprime(number):
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False

        for _ in range(3, int(number ** 0.5) + 1, 2):
            if number % _ == 0:
                return False

        return True

    phi = (1 + 5 ** 0.5) / 2
    m = phi ** n
    a, b = int(m), int(m) + 1
    a_ = a ** 2 + 3 * b ** 2
    b_ = 2 * a * b + 3 * a

    while a_ % 5 != 0 or not isprime(a_):
        a, b = a_ / b_, b_ - a_ / b_ * (a + 2 * b)
        a_, b_ = a ** 2 + 3 * b ** 2, 2 * a * b + 3 * a

    return a_

