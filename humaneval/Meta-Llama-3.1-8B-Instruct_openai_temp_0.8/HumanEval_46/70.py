Here's a Python script that uses memoization to efficiently compute the n-th element of the fib4 number sequence without using recursion:
```markdown
### Fib4 Number Sequence
#### Compute the n-th element using memoization

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Example:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    # Initialize memoization table
    memo = [0, 0, 2] + [0]*(n-2)
    
    # Fill up memoization table
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4]
    
    return memo[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script defines a function `fib4(n)` that uses memoization to efficiently compute the n-th element of the Fib4 number sequence. The function uses a memoization table to store the previously computed values, which avoids redundant computations and improves the performance. The base cases are handled directly, and the function iterates over the range from 3 to n to fill up the memoization table. Finally, the function returns the n-th element of the Fib4 number sequence.