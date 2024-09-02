

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
    def fib(n: int, memo: dict = {}):
        if n in memo:
            return memo[n]
        else:
            a, b = 0, 1
            result = a
            for i in range(n-1, -1, -1):
                result = fib(i, memo) + fib(i+1, memo)
            memo[n] = result
            return result

    return fib(n, {})

@cuda.jit
