

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
    memo = [0, 1, 1]
    index = 2
    while True:
        memo.append(memo[index] + memo[index - 1])
        index += 1
        if is_prime(memo[index]):
            if n == 1:
                return memo[index]
            n -= 1

