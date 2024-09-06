

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
    # A Fibonacci sequence is defined by the recurrence relation
    # f(n) = f(n-1) + f(n-2)
    # where f(0) = 0 and f(1) = 1
    # The first n numbers in the sequence are:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    #
    # We can check whether a number is prime by using the Sieve of Eratosthenes
    #
    # Let's consider the case of the n-th number in the sequence.
    # It's prime if:
    # 1. It's not divisible by any of the first n/2 numbers
    # 2. It's not divisible by any of the first n/2 numbers
    #
    # To check if n is prime, we can call the function prime_fib(n-1) and
    # prime_fib(n-2) and check if the result is equal to n. If it is, then
    # n is prime, otherwise, it is not.
    #
    # This algorithm is not very efficient, as we have to check all the numbers
    # in the Fibonacci sequence up to the n-th one. A better way to solve this
    # problem is to use a prime number generator like the Sieve of Sundaram
    # or the Sieve of Atkin.
    #
    # But, for learning purposes, let's solve it using this simple method.
    #
    # Here's the Python code for the function prime_fib:
    for j in range(n):
        if n % j:
            return j
    return n
