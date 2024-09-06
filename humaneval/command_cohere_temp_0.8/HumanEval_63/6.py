```python
def fibfib(n):
    # Create a memoization dictionary with initial values:
    # 0 at indices 0 and 1, and 1 at index 2.
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n + 1):
        # Compute the next value in the sequence using the definition:
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]

# Test cases:
# Check the first few elements of the sequence:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This code defines the `fibfib` function, which uses memoization to efficiently compute the n-th element of the FibFib sequence, as per the sequence's definition. The test cases are included to validate the correctness of the implementation against known output values. Just copy and paste this code into a Python environment or script to use it.