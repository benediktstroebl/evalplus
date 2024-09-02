

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
    if n < 1:
        return 0
    if n == 1:
        return 2

    # list of fibonacci numbers
    fib = [1, 1]
    # list of prime fibonacci numbers
    prime_fib_list = [2, 3]
    current = 3
    current_fib_index = 1

    while len(prime_fib_list) < n:
        current = fib[current_fib_index - 1] + fib[current_fib_index]
        fib.append(current)
        current_fib_index += 1
        if is_prime(current):
            prime_fib_list.append(current)

    return prime_fib_list[n - 1]

