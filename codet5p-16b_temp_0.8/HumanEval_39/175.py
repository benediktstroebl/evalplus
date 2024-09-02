

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

    fib_numbers = [1, 1]
    last_num = 2
    while len(fib_numbers) < n:
        next_num = last_num + fib_numbers[-1]
        fib_numbers.append(next_num)
        last_num = next_num % fib_numbers[-2] if next_num % fib_numbers[-2]!= 0 else fib_numbers[-2]

    if len(fib_numbers) == n:
        return last_num
    else:
        return None
