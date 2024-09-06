

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
        return 2
    elif n < 11:
        return 1
    elif n % 2 == 0:
        return 3
    elif n % 3 == 0:
        return 5
    elif n > 127:
        # The last condition is to handle large number of Fibonacci sequence
        # as Python's maximum integer value is 2147483647
        # Therefore, we have to check if it is prime or not.
        # We can use a simple Sieve of Eratosthenes algorithm
        # to check if a number is prime.
        # We can also use a library like prime (from the prime package)
        # to check if a number is prime.
        # Here, we are just checking the number is prime manually
        # by checking if it is divisible by any number other than 2 and 3.
        divisors = 1
        for i in range(5, int(math.sqrt(n)) + 1):
            divisors *= i
        return n % (divisors * (divisors - 1) // 2)
