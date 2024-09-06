

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
    fib_list = [1, 2]

    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    if n <= 0:
        return None
    elif n == 1:
        return 2
    else:
        fib_list_size = 2
        while fib_list_size <= n:
            fib_list_size += 1
            fib_list.append(fib_list[fib_list_size - 2] + fib_list[fib_list_size - 1])
        for i in range(1, fib_list_size - 1):
            if is_prime(fib_list[i]):
                if is_prime(fib_list[i - 1]):
                    if is_prime(fib_list[i + 1]):
                        return fib_list[i]

