

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
    if n <= 1:
        return None
    # think: fib(n) = fib(n-1) + fib(n-2)
    fib_num = [1, 2]
    curr_fib = 2
    while True:
        num_to_check = curr_fib + fib_num[-2]
        if num_to_check > n:
            break
        if is_prime(num_to_check):
            fib_num.append(num_to_check)
            curr_fib = num_to_check
    return fib_num[n - 1]

