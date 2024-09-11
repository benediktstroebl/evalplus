### FibFib Number Sequence
The FibFib number sequence is a sequence similar to the Fibonacci sequence, with the recurrence relation defined as:

fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

We will use memoization to store previously computed values to efficiently compute the n-th element of the sequence.

```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    # Initialize a dictionary to store memoized values
    memo = {0: 0, 1: 0, 2: 1}
    
    # Define a helper function to perform the memoized computation
    def fibfib_helper(k: int) -> int:
        # If the value is already memoized, return it
        if k in memo:
            return memo[k]
        
        # Otherwise, compute the value and store it in the memo dictionary
        else:
            result = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
            memo[k] = result
            return result
    
    # Return the n-th element of the sequence
    return fibfib_helper(n)

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a dictionary `memo` to store previously computed values of the Fibonacci sequence, which significantly improves the performance of the function for large inputs. The `fibfib_helper` function is a recursive helper function that uses memoization to compute the n-th element of the sequence.