### FibFib Number Sequence Calculator
#### Problem Description
The FibFib number sequence is a sequence similar to the Fibonacci sequence, but with a different recurrence relation. We need to write a function to efficiently compute the n-th element of the FibFib number sequence.

#### Code
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence, 
    but with a different recurrence relation. This function efficiently computes 
    the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element in the FibFib sequence to compute.

    Returns:
    int: The n-th element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo = {0: 0, 1: 0, 2: 1}
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
#### Explanation
This script uses dynamic programming and memoization to efficiently compute the n-th element of the FibFib sequence. It creates a dictionary `memo` to store the computed elements and their indices. It then iteratively computes the elements from 3 to `n` using the recurrence relation, storing the result in the `memo` dictionary. Finally, it returns the n-th element from the `memo` dictionary. This approach avoids redundant computations and improves performance.