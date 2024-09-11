```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the Fibonacci sequence to be computed.

    Returns:
        int: The nth element of the FibFib number sequence.

    Raises:
        ValueError: If n is less than 0.

    Example:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
if __name__ == "__main__":
    for i in range(1, 9):
        print(f"fibfib({i}) = {fibfib(i)}")
```
This script defines the `fibfib` function, which efficiently computes the nth element of the FibFib number sequence. The function uses dynamic programming to store previous values, reducing the time complexity of each recursive call. It also includes test cases to verify the correctness of the function.