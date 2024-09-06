

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
    if n < 2:
        return 2

    if n % 2 == 0:
        return 3

    if n % 3 == 0:
        return 5

    candidate = 2
    last = 0

    while True:
        next = last + candidate

        if next > n:
            break

        if next - 1 in prime_fib_cache.values():
            return next - 1

        if prime(next) and (next > 2 or next - 1 not in prime_fib_cache.values()):
            prime_fib_cache[candidate] = n - 1
            return n - 1

        candidate = next
        last = next + 1

    return prime_fib_cache[candidate]

prime_fib_cache = {}

for candidate in range(2, int(sqrt(2 * (prime_fib(5))) + 1) ** 2):
    if prime(candidate):
        prime_fib_cache[candidate] = candidate
