Here's a Python script that uses memoization to efficiently compute the n-th element of the FibFib number sequence:
```markdown
### FibFib Number Sequence

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

#### Code

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.

    Raises:
    ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Create a dictionary to store the memoized results
    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_recursive(i: int) -> int:
        """
        Compute the i-th element of the FibFib number sequence recursively.

        Args:
        i (int): The index of the element to compute.

        Returns:
        int: The i-th element of the FibFib number sequence.
        """
        # Check if the result is already memoized
        if i in memo:
            return memo[i]
        else:
            # Compute the result recursively and memoize it
            result = fibfib_recursive(i-1) + fibfib_recursive(i-2) + fibfib_recursive(i-3)
            memo[i] = result
            return result

    return fibfib_recursive(n)

#### Example Usage

print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a recursive approach with memoization to efficiently compute the n-th element of the FibFib number sequence. The `fibfib_recursive` function is used to compute the i-th element recursively, and the memoized results are stored in a dictionary called `memo`. The `fibfib` function is the main entry point, and it uses the `fibfib_recursive` function to compute the n-th element. The script includes example usage and docstrings to make it easier to understand.