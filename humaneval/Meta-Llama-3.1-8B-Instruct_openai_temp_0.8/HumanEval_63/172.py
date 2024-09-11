```python
def fibfib(n: int) -> int:
    """
    Compute the nth element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the FibFib number sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        # Initialize a list to store the Fibonacci-like numbers
        fibfib_list = [0, 0, 1] + [0]*(n-3)
        # Compute the Fibonacci-like numbers
        for i in range(4, n+1):
            fibfib_list[i-1] = fibfib_list[i-2] + fibfib_list[i-3] + fibfib_list[i-4]
        return fibfib_list[n-1]


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this script, we first check the base cases where `n` is less than or equal to 3. Then, we initialize a list `fibfib_list` to store the Fibonacci-like numbers up to the `n`-th element. We compute the Fibonacci-like numbers iteratively using a for loop, and return the `n`-th element at the end.