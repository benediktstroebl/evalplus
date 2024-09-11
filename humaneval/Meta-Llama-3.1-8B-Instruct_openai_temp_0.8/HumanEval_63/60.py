```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's 
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the number in the FibFib sequence.
    
    Returns:
        int: The n-th number in the FibFib sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 0:
        raise ValueError("n must be a non-negative integer")
    else:
        # Create a dictionary to store the computed values
        memo = {0: 0, 1: 0, 2: 1}
        
        for i in range(3, n + 1):
            # Compute the i-th value in the sequence
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        
        return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a function `fibfib(n)` to compute the n-th number in the FibFib sequence. It uses a dictionary `memo` to store the computed values, so that they can be looked up quickly rather than recomputed every time they are needed. This makes the function much more efficient for large values of `n`.

The function first checks the base cases where `n` is 0, 1, or 2. For larger `n`, it iterates from 3 to `n` and computes the `i-th` value in the sequence as the sum of the three preceding values. The computed value is then stored in the `memo` dictionary for future use.