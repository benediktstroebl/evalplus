

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

    # Write your code here
    a, b = 0, 1
    prime_list = [2, 3]
    nth_fib = 1
    while True:
        nth_fib = (a + b) % 1000000007
        if nth_fib in prime_list:
            a, b = b, nth_fib
        else:
            prime_list.append(nth_fib)
            a, b = b, nth_fib

        if len(prime_list) == n:
            return nth_fib
