Here's a Python script that uses an iterative approach to calculate the n-th element of the fib4 number sequence:

```markdown
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the number in the sequence to be calculated.

    Returns:
        int: The n-th number in the fib4 sequence.
    """
    if n <= 3:
        # base cases
        return [0, 0, 2, 0][n]

    # initialize a list to store the sequence
    sequence = [0] * (n + 1)
    sequence[1] = 0
    sequence[2] = 2
    sequence[3] = 0

    # calculate the rest of the sequence
    for i in range(4, n + 1):
        sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3] + sequence[i-4]

    return sequence[n]


# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses a list `sequence` to store the calculated numbers in the sequence. The base cases are handled separately, and then the rest of the sequence is calculated iteratively. This approach avoids the performance issues associated with recursive function calls.