```markdown
### Efficiently Computing the n-th Element of the FibFib Number Sequence

The following Python script uses a technique called memoization to efficiently compute the n-th element of the FibFib number sequence.

```python
def fibfib(n: int, memo = {}) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the desired element in the FibFib sequence.
        memo (dict, optional): A dictionary to store previously computed values. Defaults to {}.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Check if the value is already computed
    elif n in memo:
        return memo[n]
    # Compute the value and store it in memo
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        memo[n] = result
        return result

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

### Explanation

The function `fibfib(n, memo)` uses a dictionary `memo` to store previously computed values. This technique is called memoization. By storing the computed values, we avoid redundant computations and improve the efficiency of the function.

The function first checks for the base cases (n == 0, n == 1, n == 2) and returns the corresponding values. If the value of `n` is already in the `memo` dictionary, it returns the stored value. Otherwise, it computes the value by recursively calling the function for `n-1`, `n-2`, and `n-3`, stores the result in the `memo` dictionary, and returns it.

This approach significantly improves the efficiency of the function by avoiding redundant computations and reducing the time complexity from exponential to linear.
```