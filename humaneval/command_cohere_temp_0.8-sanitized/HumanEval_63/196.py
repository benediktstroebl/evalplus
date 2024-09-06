from collections import Iterator
class FibFibIterator(Iterator):
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            self.a = 0
        elif self.n == 1:
            self.a = 0
            self.b = 0
        elif self.n == 2:
            self.a = 0
            self.b = 1
        else:
            self.a = self.a + self.b + self.fib3(self.n - 3)
            self.b = self.a + self.fib3(self.n - 2)
            self.a = self.a + self.fib3(self.n - 1)
        self.n -= 1
        return self.a

    def fib3(self, n):
        a, b, c = 0, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Find the n-th element of the FibFib sequence efficiently using the generator function below.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    return next(FibFibIterator(n))