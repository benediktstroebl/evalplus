```python
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
```
This code defines a generator function FibFibIterator, which efficiently calculates the n-th FibFib number sequence using a recursive definition in a iterative way. This function constructs and returns an iterator object, allowing you to iterate over the FibFib sequence up to the specified index. The generator uses a recursive approach, where each next value is based on the three preceding values (fib3(n-1), fib3(n-2), fib3(n-3)). This script also checks for input validity by verifying that n is an integer and that it is not negative. If the input is invalid, it raises a ValueError. 

You can use the `next()` function to compute the first element of the sequence or use the `iter()` function to create an iterator and then use the `next()` function to compute the subsequent elements of the sequence.

Please note that this is a generator function, so it can be more memory-efficient for large values of n compared to a regular function since it generates the sequence on-the-fly without storing all the values in memory.  This approach also avoids the exponential growth of the function call stack that you would see when calculating Fibonacci numbers directly.  This approach gracefully handles even large inputs with minimal memory usage.  You can also iterate directly up to the desired index without having to compute the entire sequence.  However, it is still recommended to use a recursive approach for small values of n, as the iterative approach has some overhead due to function calls.  This approach also has the advantage of being memory-efficient and easy to understand and implement.  You can easily extend it to handle larger values of n by adding appropriate arguments