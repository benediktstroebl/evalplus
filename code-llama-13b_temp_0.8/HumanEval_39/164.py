

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
    num1, num2 = 1, 1
    prime_fib_seq = [num1, num2]
    if n == 1:
        return num1
    elif n == 2:
        return num2
    while True:
        next_num = num1 + num2
        prime_fib_seq.append(next_num)
        num1 = num2
        num2 = next_num
        if is_prime(next_num) and is_fibonacci(next_num):
            if len(prime_fib_seq) >= n:
                return prime_fib_seq[n]

