

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
    fib_cache = [0, 1, 1]
    prime_cache = [2, 3]
    cur_num = 3
    cur_fib_idx = 1
    cur_prime_idx = 1
    while cur_prime_idx < n:
        cur_fib_idx += 1
        cur_num = fib_cache[cur_fib_idx]
        is_prime = True
        i = 0
        while prime_cache[i]**2 < cur_num:
            if cur_num % prime_cache[i] == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            prime_cache.append(cur_num)
            cur_prime_idx += 1
        fib_cache.append(cur_num)
    return prime_cache[n-1]

