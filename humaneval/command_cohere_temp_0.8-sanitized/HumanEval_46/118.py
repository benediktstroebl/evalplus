def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    """
    # Define the cache with 4 elements, initialize to zeros.
    cache = [0, 0, 2, 0]
    for i in range(4, n + 1):
        cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3] + cache[i - 4])
    return cache[n]