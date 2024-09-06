

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
    assert (n > 0), "n must be positive"
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        k = 3
        n_minus_1 = 1
        n_minus_2 = 2
        while n_minus_1 + n_minus_2 < n:
            k += 1
            n_minus_2 = n_minus_1
            n_minus_1 = k * (k-1) / 2
        if n <= n_minus_1 + n_minus_2:
            n_minus_2 = n_minus_1
            n_minus_1 = k * (k-1) / 2
            k -= 1
        check_divisors = [k, n_minus_1]
        possible_divisors = [x for x in check_divisors if x < n]
        for i in possible_divisors:
            if (n % i == 0):
                return i
        return None

