```markdown
### FibFib Number Sequence
#### Computing the n-th element efficiently using dynamic programming

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_cache = [0] * (n + 1)
        fibfib_cache[0] = 0
        fibfib_cache[1] = 0
        fibfib_cache[2] = 1
        for i in range(3, n + 1):
            fibfib_cache[i] = fibfib_cache[i-1] + fibfib_cache[i-2] + fibfib_cache[i-3]
        return fibfib_cache[n]


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines the `fibfib` function to compute the n-th element of the FibFib sequence using dynamic programming to store previously computed values in a cache array. The function uses the base cases provided and iteratively calculates the subsequent elements based on the recursive definition. The test cases at the end demonstrate the function's correctness.

Note: This implementation has a time complexity of O(n) and a space complexity of O(n) due to the cache array. For large values of n, a more efficient implementation may be needed to avoid excessive memory usage.