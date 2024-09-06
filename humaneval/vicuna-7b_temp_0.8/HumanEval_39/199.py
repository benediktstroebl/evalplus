

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
        return n

    def is_prime(x):
        if x == 0 or x == 1:
            return False
        elif x % 2 == 0:
            return False
        else:
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

    fibonacci = [0, 1]
    prev = 0
    for i in range(2, int(n ** 0.5) + 1):
        fibonacci.append(prev)
        prev = fibonacci[-1] + fibonacci[-2]

    prime_fib_list = []
    for i in range(1, int(n ** 0.5) + 1):
        if is_prime(fibonacci[-1]):
            prime_fib_list.append(fibonacci[-1])

    return prime_fib_list[-1]