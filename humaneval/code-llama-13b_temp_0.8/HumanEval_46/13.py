

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError(f'n must be a positive integer')
    # initilize a cache to store computed fib4 values
    cache = dict()
    # fill in the cache
    cache[0] = 0
    cache[1] = 0
    cache[2] = 2
    cache[3] = 0
    for i in range(4, n+1):
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3] + cache[i-4]
    # return the value for n
    return cache[n]

