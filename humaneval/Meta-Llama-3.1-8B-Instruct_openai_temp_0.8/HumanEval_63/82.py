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
    n (int): The position of the element in the sequence to compute.

    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n <= 2:  # Base cases
        return 0 if n == 1 else 1
    memo = {0: 0, 1: 0, 2: 1}  # Store computed values in a dictionary

    def fibfib_recursive(k: int) -> int:
        """Recursive helper function to compute the k-th element."""
        if k not in memo:  # If value not in memo, compute and store it
            memo[k] = fibfib_recursive(k-1) + fibfib_recursive(k-2) + fibfib_recursive(k-3)
        return memo[k]

    return fibfib_recursive(n)  # Start the recursion from n

# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script uses a recursive approach to compute the nth element of the FibFib sequence. It takes advantage of memoization (storing computed values in a dictionary) to avoid redundant computations and improve performance.

However, this recursive approach may lead to excessive function calls and is not optimal for large values of n. A more efficient solution would be to use dynamic programming with an iterative approach.

Here's an alternative implementation:

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    """
    if n <= 2:
        return 0 if n == 1 else 1

    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, b + c + a

    return c

# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This iterative solution avoids function calls and uses a constant amount of space to compute the nth element of the FibFib sequence. It is more efficient than the recursive approach and can handle large values of n.