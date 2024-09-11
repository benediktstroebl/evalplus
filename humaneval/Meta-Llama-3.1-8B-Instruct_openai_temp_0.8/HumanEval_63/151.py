```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The nth element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed FibFib numbers
    fibfib_nums = [0] * (n + 1)
    fibfib_nums[0] = 0
    fibfib_nums[1] = 0
    fibfib_nums[2] = 1

    # Compute the FibFib numbers iteratively
    for i in range(3, n + 1):
        fibfib_nums[i] = fibfib_nums[i - 1] + fibfib_nums[i - 2] + fibfib_nums[i - 3]

    return fibfib_nums[n]


# Test the function
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This code defines a function `fibfib(n)` that efficiently computes the nth element of the FibFib number sequence. It uses a bottom-up dynamic programming approach to store and reuse the computed values of the sequence. The function takes an integer `n` as input and returns the corresponding FibFib number. The code also includes test cases to verify the correctness of the function.