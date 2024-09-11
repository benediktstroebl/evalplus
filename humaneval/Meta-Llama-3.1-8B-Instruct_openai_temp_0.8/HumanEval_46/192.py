### Fib4 Number Sequence Computation

Below is a self-contained Python script that efficiently computes the n-th element of the fib4 number sequence without using recursion.

```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element in the fib4 sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib4_prev_prev_prev_prev = 0
    fib4_prev_prev_prev = 0
    fib4_prev_prev = 2
    fib4_prev = 0

    for _ in range(4, n + 1):
        fib4_curr = (
            fib4_prev_prev_prev_prev
            + fib4_prev_prev_prev
            + fib4_prev_prev
            + fib4_prev
        )
        fib4_prev_prev_prev_prev = fib4_prev_prev_prev
        fib4_prev_prev_prev = fib4_prev_prev
        fib4_prev_prev = fib4_prev
        fib4_prev = fib4_curr

    return fib4_prev
```

This script uses an iterative approach to compute the n-th element of the fib4 number sequence. It initializes variables to hold the last four elements of the sequence and then iteratively updates them to compute the next element. The function has a time complexity of O(n), making it efficient for large values of n.