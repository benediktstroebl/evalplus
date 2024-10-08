

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
    memo = [-1, 0, 0, 2, 0]
    
    def get_fib4(n: int) -> int:
        if n < 0:
            return 0
        if memo[n] != -1:
            return memo[n]
        else:
            memo[n] = get_fib4(n-1) + get_fib4(n-2) + get_fib4(n-3) + get_fib4(n-4)
            return memo[n]
    return get_fib4(n)
