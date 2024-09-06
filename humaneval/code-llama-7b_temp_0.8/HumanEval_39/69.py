

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

    # This solution is really ugly and it's based on the knowledge that 2 is the first prime Fibonacci number.
    # The solution should be changed when the knowledge is better understood.

    def is_prime(number):
        if number < 2:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            for i in range(3, int(number ** 0.5) + 1, 2):
                if number % i == 0:
                    return False
            return True

    if n == 1:
        return 2

    k = 0
    while True:
        k += 1
        nth_fib = fibonacci(k)
        if is_prime(nth_fib):
            return nth_fib

