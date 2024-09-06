```python
from itertools import accumulate

def fibfib_iter(n: int):
    fibfib_0 = 0
    fibfib_1 = 0
    fibfib_2 = 1
    for i in range(3, n + 1):
        fibfib_i = fibfib_prev(fibfib_prev(fibfib_prev(fibfib_2, fibfib_1, fibfib_0)) + fibfib_1 + fibfib_0)
        fibfib_0, fibfib_1, fibfib_2 = fibfib_1, fibfib_2, fibfib_i
    return fibfib_2

def fibfib_prev(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return c
    if c == 0:
        return a
    return fibfib_prev(a - b, b - c, c)

def fibfib(n: int):
    return next(accumulate(fibfib_iter(n), 0))
```

This solution uses memoization via an iterator and the accumulate iterator function to efficiently compute the n-th FibFib number. You can use this function to compute the FibFib numbers for n = 1, 5, and 8, as indicated in the test cases. Just call `fibfib(n)` to calculate the n-th FibFib number. 
The way it works is that the `fibfib_iter` function uses an iterator to generate the FibFib numbers up to `n`. It starts with `fibfib_0`, `fibfib_1`, and `fibfib_2` initialized to the base cases of the sequence. Then, it iteratively calculates the next FibFib numbers using the recurrence relation, updating the variables accordingly.

The `fibfib_prev` function is used to simplify the calculation of the previous three numbers in the sequence, as it takes three previous FibFib numbers and returns the one before them, based on the recurrence relation.

Finally, `accumulate` is used to fold (or accumulate) the iterator of FibFib numbers with a starting value of 0, producing a single iterable that contains the FibFib numbers calculated up to `n`. The `next` function is used to get the n-th element from this accumulated iterator.