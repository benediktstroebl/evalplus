

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
    if n < 1:
        return 0

    fib_numbers = [0, 1]
    cur_pos = 2
    while True:
        num = fib_numbers[cur_pos - 1] + fib_numbers[cur_pos - 2]
        fib_numbers.append(num)
        if num > 10**999:
            break
        cur_pos += 1
    prime_fibs = [2]
    cur_pos = 1
    cur_num = 3
    while True:
        if is_prime(cur_num):
            prime_fibs.append(cur_num)
            if len(prime_fibs) == n:
                return prime_fibs[-1]
        cur_num += 2

