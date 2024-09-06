

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
    # 2-3-5 と 8-13-8 の結果が同じである場合は該当する
    if n == 2 or n == 3 or n == 5 or n == 8 or n == 13 or n == 18:
        return n * (n - 1) * (n - 2)
    else:
        a, b = fibonacci(n - 1), fibonacci(n - 2)
        return a + b + fibonacci(n - 3)
