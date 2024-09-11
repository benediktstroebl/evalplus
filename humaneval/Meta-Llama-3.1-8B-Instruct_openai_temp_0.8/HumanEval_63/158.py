Here's a Python script that calculates the FibFib number sequence efficiently using memoization.

```markdown
### FibFib Number Sequence
#### Efficient Computation Using Memoization

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

Here's a Python function that efficiently computes the n-th element of the FibFib number sequence using memoization.

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    - fibfib(0) == 0
    - fibfib(1) == 0
    - fibfib(2) == 1
    - fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the sequence to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    memo = {0: 0, 1: 0, 2: 1}  # Initialize the memoization dictionary
    
    def fibfib_helper(k: int) -> int:
        """
        Helper function to compute the k-th element of the FibFib sequence using memoization.
        
        Args:
            k (int): The position of the element in the sequence to compute.
        
        Returns:
            int: The k-th element of the FibFib number sequence.
        """
        if k not in memo:
            # If the k-th element is not in the memoization dictionary, compute it and store it in the dictionary
            memo[k] = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
        return memo[k]
    
    return fibfib_helper(n)

# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses memoization to store the values of previously computed elements in a dictionary, which significantly improves performance for large values of `n`.