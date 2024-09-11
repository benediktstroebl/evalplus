```markdown
### FibFib Number Sequence
#### Efficiently compute the n-th element of the FibFib number sequence.

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
- fibfib(0) == 0
- fibfib(1) == 0
- fibfib(2) == 1
- fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows: fibfib(0) == 0, fibfib(1) == 0, fibfib(2) == 1, 
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the FibFib sequence.

    Returns:
        int: The nth element of the FibFib sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the results of subproblems
    memo = [0, 0, 1] + [0]*(n-2)

    # Fill up the memo list
    for i in range(3, n+1):
        # For each number, calculate its value and store it in the memo list
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    # Return the nth element of the FibFib sequence
    return memo[n]
```

### Example Usage
```python
# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
This script uses dynamic programming to efficiently compute the nth element of the FibFib number sequence. It first checks for base cases and then uses a list (memo) to store the results of subproblems, which are calculated only once and stored for future use. This approach avoids redundant calculations and makes the function much more efficient for large values of n.