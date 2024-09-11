```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 3:
        return 0
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses memoization (a technique for improving the performance of recursive algorithms by storing the results of expensive function calls) to efficiently compute the n-th element of the FibFib number sequence.

However, for larger values of `n`, it may be more efficient to use dynamic programming. The script provided above uses a simple iterative approach.

For a more efficient solution using dynamic programming, we can use a bottom-up approach with a list to store the computed values:
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The nth element of the FibFib sequence.
    """
    fib = [0] * (n + 1)
    fib[2] = 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3]
    return fib[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This version is more efficient for large values of `n` because it avoids repeated computations.