

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
    fib_nums = [2, 3]
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    for num in range(2, int(n ** 0.5) + 1):
        if is_prime[num]:
            for i in range(num * 2, n + 1, num):
                is_prime[i] = False
    for num in range(2, n + 1):
        if is_prime[num]:
            fib_nums.append(num)
    return fib_nums[-1]

