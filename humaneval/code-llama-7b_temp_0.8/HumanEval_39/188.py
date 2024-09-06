

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
    # Fibonacci series:
    # fn = fn-1 + fn-2

    # First and second numbers are prime numbers.
    # So, let's check only these numbers.
    #
    # fn-1 = a-1
    # fn-2 = a
    # fn = a + a-1 = 2*a -1
    #
    # If n-th number is Fibonacci number - it is a prime number.
    # So, we can find the n-th number using this formula.
    #
    # For example, if n = 5 - the fifth Fibonacci number is 5, and it is also prime.
    # So, we can calculate a using the following formula:
    # a = round(math.sqrt(5))
    #
    # Let's check, if a is a Fibonacci number:
    # a^2 = a^2 - 2*a + 1
    # 0 = 2*a - 1
    # a = 1
    # a is a Fibonacci number
    #
    # Let's check, if a-1 is a Fibonacci number:
    # a-1^2 = (a-1)^2 - 2*(a-1) + 1
    # 0 = -2*a + 2
    # a = 2
    # a-1 is a Fibonacci number
    #
    # The formula for n-th Fibonacci number is:
    # n*(2^n - 1)/(n+1)
    #
    # The n-th number is a Fibonacci number, if it is prime.
    # So, we can check, if it is a prime number using Sieve of Eratosthenes.
    #
    # We know that all prime numbers are less than 2^n.
    # So, we can create an array of 2^n size and use Sieve of Eratosthenes.
    # It takes a lot of time, but this task is from "Easy" section.
    #
    from math import sqrt

    if n == 1:
        return 2
