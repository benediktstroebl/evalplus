

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
    # start_time = time.time()

    prime_list = [2]
    nums = [1, 2]

    while len(prime_list) <= n:
        nums.append(nums[-2] + nums[-1])
        if is_prime(nums[-1]):
            prime_list.append(nums[-1])

    # end_time = time.time()
    # print("total time: ", end_time - start_time)

    return prime_list[n]

