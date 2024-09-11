Here is a Python script that calculates the n-th element of the FibFib sequence efficiently using dynamic programming:
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    fibfib_values = [0, 0, 1]
    for i in range(3, n + 1):
        fibfib_values.append(fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3])
    return fibfib_values[n]


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
This script calculates the n-th element of the FibFib sequence by building up a list of previously computed values using dynamic programming. This approach allows us to avoid redundant calculations and compute the result efficiently.

Note that the time complexity of this algorithm is O(n), making it much faster than a naive recursive approach with a time complexity of O(2^n).