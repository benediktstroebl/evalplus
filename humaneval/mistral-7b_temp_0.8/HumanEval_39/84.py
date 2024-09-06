

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
    num_list = [0, 1]
    for i in range(2, n):
        if is_prime(num_list[i]) and is_prime(num_list[i - 1]):
            return num_list[i]
        num_list.append(num_list[i - 1] + num_list[i - 2])

