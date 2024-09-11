### FibFib Number Sequence Calculator

Below is a Python script that calculates the n-th element of the FibFib number sequence efficiently using memoization.

```markdown
### Code
```python
def fibfib(n: int, memo: dict = {}) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the number in the sequence.
    memo (dict, optional): A dictionary to store previously computed values. Defaults to {}.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        memo[n] = result
        return result

### Example Usage
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

### Explanation

The `fibfib` function uses memoization to store previously computed values in the `memo` dictionary. This approach significantly improves the efficiency of the function by avoiding repeated calculations.

The function follows the definition of the FibFib sequence and handles edge cases (n <= 0, n == 1, n == 2) separately. For larger values of n, it recursively calculates the result by adding the previous three numbers in the sequence. The result is then stored in the `memo` dictionary to avoid repeated calculations.

The example usage demonstrates how to call the `fibfib` function with different values of n and print the results.