```markdown
### FibFib Number Sequence
#### Problem Description
The FibFib number sequence is a sequence similar to the Fibonacci sequence, defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

#### Solution
We can use memoization to efficiently compute the n-th element of the FibFib number sequence.

```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    memo = {0: 0, 1: 0, 2: 1}  # Initialize the memo dictionary

    def fibfib_rec(k: int):
        """
        Recursive function to compute the k-th element of the FibFib number sequence.

        Args:
        k (int): The index of the element to compute.

        Returns:
        int: The k-th element of the FibFib number sequence.
        """
        if k not in memo:  # If the k-th element is not in the memo dictionary
            memo[k] = fibfib_rec(k-1) + fibfib_rec(k-2) + fibfib_rec(k-3)  # Compute it recursively
        return memo[k]

    return fibfib_rec(n)

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this solution, we use a recursive function `fibfib_rec` to compute the k-th element of the FibFib number sequence. We store the computed elements in a memo dictionary to avoid redundant computations and improve efficiency.

The time complexity of this solution is O(n), and the space complexity is also O(n) due to the memo dictionary.