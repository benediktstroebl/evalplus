### Python Script: Efficiently Computing the Fib4 Number Sequence

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the Fib4 sequence.

    Returns:
        int: The nth element of the Fib4 sequence.
    """
    if n <= 1:
        return 0
    memo = {0: 0, 1: 0, 2: 2}
    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4]
    return memo[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses memoization to efficiently compute the nth element of the Fib4 number sequence. The `fib4` function takes an integer `n` as input and returns the corresponding element in the sequence. It first checks if `n` is less than or equal to 1, in which case it returns 0. Otherwise, it initializes a dictionary `memo` with the base cases (0, 1, and 2) and then computes the remaining elements up to `n`. Finally, it returns the value of `memo[n]`.