### Efficiently Computing the FibFib Number Sequence
#### Using Memoization for Optimal Performance

Below is a Python script that efficiently computes the n-th element of the fibfib number sequence using memoization to store previously computed values.

```markdown
def fibfib(n: int, memo={}):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element in the FibFib sequence to compute.
        memo (dict, optional): A dictionary to store previously computed values. Defaults to {}.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    
    # Base cases
    if n in [0, 1]:
        return 0
    elif n == 2:
        return 1
    
    # Check if value is already computed
    if n not in memo:
        # Compute value and store it in memo
        memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    
    return memo[n]

# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a dictionary (`memo`) to store previously computed values, allowing the function to avoid redundant computations and significantly improve its performance for larger inputs.