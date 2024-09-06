

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
        return 0
    if n < 10:
        return n
    if n % 2 == 0:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 3
    a = 0
    b = 1
    for i in range(2, n):
        if n % i == 0:
            return 0
        if n % i == 2:
            a = a + (i-2)
        elif n % i == 1:
            b = b + (i-1)
        i = i + 1
    a = a + (n-2)
    a = a + b
    return a

if __name__ == "__main__":
    for i in range(65537):
        n = i + 1
        if prime_fib(n) > 0:
            prime_numbers.append(n)
