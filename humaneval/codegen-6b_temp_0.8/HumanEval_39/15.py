

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
    memo = {}
    def fib(n):
        if n in memo:
            return memo[n]
        if n == 1:
            ans = 1
        elif n % 2 == 0:
            ans = fib(n - 1) + fib(n - 2)
        else:
            ans = fib(n - 1) + fib(n - 2) + 2 * fib(n - 3)
        memo[n] = ans
        return ans

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        for num in range(3, int(n**0.5) + 1, 2):
            if n % num == 0:
                return False
        return True

    cnt = 0
    curr = 1
    while 1:
        curr = fib(cnt)
        if is_prime(curr):
            cnt += 1
        else:
            return curr
