

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
    numbers = [2, 3]
    if n == 1:
        return 2
    if n == 2:
        return 3
    for i in range(n - 2):
        num = numbers[i] + numbers[i + 1]
        if num % 2 != 0:
            numbers.append(num)
            if is_prime(num):
                return num
    raise ValueError(f"No Fibonacci numbers that are prime are found up to {n}")

