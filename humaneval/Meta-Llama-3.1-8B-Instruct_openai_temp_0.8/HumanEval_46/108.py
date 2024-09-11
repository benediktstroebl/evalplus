### Fib4 Number Sequence Computation

Here's a Python script that efficiently computes the n-th element of the fib4 number sequence using dynamic programming.

```markdown
### fib4.py

```python
def fib4(n: int) -> int:
    """
    Computes the n-th element of the fib4 number sequence.

    The fib4 number sequence is a sequence defined as follows:
    - fib4(0) -> 0
    - fib4(1) -> 0
    - fib4(2) -> 2
    - fib4(3) -> 0
    - fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    Args:
        n (int): The index of the element in the sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib_values = [0, 0, 2, 0] + [0] * (n - 3)
        for i in range(4, n + 1):
            fib_values[i - 1] = fib_values[i - 1] + fib_values[i - 2] + fib_values[i - 3] + fib_values[i - 4]
        return fib_values[n - 1]


# Example usage:
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses dynamic programming to store and reuse previously computed values in the `fib_values` list, avoiding redundant calculations and reducing the time complexity of the function. The function handles edge cases where `n` is 0, 1, or 2, and returns the corresponding values. For larger `n`, it uses a loop to compute the values of the fib4 sequence iteratively.