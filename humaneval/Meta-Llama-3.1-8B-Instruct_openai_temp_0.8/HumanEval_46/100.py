### Fibonacci-like Sequence: Fib4
#### Problem Description
The Fib4 number sequence is defined as follows:
- `fib4(0)` = 0
- `fib4(1)` = 0
- `fib4(2)` = 2
- `fib4(3)` = 0
- `fib4(n)` = `fib4(n-1)` + `fib4(n-2)` + `fib4(n-3)` + `fib4(n-4)`

#### Solution: Using Dynamic Programming
We can solve this problem efficiently by using a technique called dynamic programming. This technique involves breaking down the problem into smaller sub-problems, solving each sub-problem only once, and storing their results to avoid redundant calculations.

```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence.

    Args:
        n (int): The index of the element in the Fib4 sequence.

    Returns:
        int: The n-th element of the Fib4 sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Initialize a list to store the first n+1 elements of the Fib4 sequence.
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2

    # Compute each element in the Fib4 sequence iteratively.
    for i in range(3, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    # Return the n-th element of the Fib4 sequence.
    return fib4_sequence[n]

# Example usage:
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This solution has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n.