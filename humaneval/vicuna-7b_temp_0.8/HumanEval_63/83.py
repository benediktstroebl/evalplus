

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    # Special case
    if n <= 3:
        return n

    # Calculate fib(n) = fib(n-1) + fib(n-2) + fib(n-3)
    # using fib(n-3) = fib(n-4) + fib(n-5) + fib(n-6)
    # and fib(n-4) = fib(n-5) + fib(n-6) + fib(n-7)
    # and so on
    #
    # This approach is inefficient and will result in an
    # exponential time complexity
    #
    # An alternative approach is to use memoization
    #
    # def fib(n):
    #     cache = {}
    #     def fib(k):
    #         if k in cache:
    #             return cache[k]
    #         if k == 0:
    #             return 0
    #         if k == 1:
    #             return 1
    #         if k in cache or (k // 2) in cache:
    #             return fib(k // 2) + fib((k // 2) + 1)
    #         else:
    #             result = fib(k - 1) + fib(k - 2) + fib(k - 3)
    #             cache[k] = result
    #             return result
    #     return fib(n)
    #
    # fib(1)
    # fib(2)
    # fib(3)
    # fib(4)
    # fib(5)
    # fib(6)
    # fib(7)
    # fib(8)

    # The memoized fib function is faster than the recursive approach
    # and has a time complexity of O(2^n)
    return fib_memo(n)
