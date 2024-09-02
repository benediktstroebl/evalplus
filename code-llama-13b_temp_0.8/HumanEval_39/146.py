

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
    phi = (1 + 5 ** 0.5) / 2
    # phi is Golden Ratio
    arr_size = int(n * phi) + 1
    # arr_size is a rough estimate of how many elements to expect
    arr = [0] * arr_size
    arr[1] = 1
    index = 2
    while index <= n:
        arr[index] = arr[index - 1] + arr[index - 2]
        if is_prime(arr[index]):
            index += 1
        else:
            arr[index] = 0
        if arr[index] == n:
            return n
    return -1

