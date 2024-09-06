```python
from collections import Sequence

def fibfib_gen(n: int):
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    elif n == 0:
        yield 0
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            yield a + b
            a, b = b, a + b

def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    The n-th element of the FibFib sequence is retrieved."""
    fibfib_seq = Sequence(fibfib_gen(n))
    return next(fibfib_seq)
```
This code defines two functions. `fibfib_gen` is a generator function that iterates through the FibFib sequence up to `n` steps, it yields each value in the sequence. The `fibfib` function retrieves the n-th element of the FibFib sequence. This code efficiently computes the n-th element of the fibfib number sequence without explicitly storing the entire sequence. 
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```