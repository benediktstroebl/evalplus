```markdown
### FibFib Number Sequence Calculator

#### Function Description
The `fibfib` function calculates the `n`-th element of the FibFib number sequence.
The FibFib sequence is defined as follows:
- `fibfib(0)` == 0
- `fibfib(1)` == 0
- `fibfib(2)` == 1
- `fibfib(n)` == `fibfib(n-1)` + `fibfib(n-2)` + `fibfib(n-3)`

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
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize memoization dictionary
    memo = {0: 0, 1: 0, 2: 1}

    # Compute and store fibfib(i) for i = 3 to n
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    # Return the n-th element
    return memo[n]


#### Example Usage

print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

#### Explanation

This script uses a technique called memoization to store the results of previous computations and avoid redundant calculations. It starts by checking the base cases and then initializes a dictionary, `memo`, to store the computed FibFib numbers. The script then iterates from `i = 3` to `n` and calculates `fibfib(i)` by using the previously computed values. Finally, it returns the `n`-th element stored in `memo`.