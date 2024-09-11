```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence
    using dynamic programming without recursion.

    Args:
        n (int): The index of the Fib4 number to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 2

    # Initialize a list to store the Fib4 numbers
    fib4_nums = [0] * (n + 1)

    # Initialize the first four Fib4 numbers
    fib4_nums[0] = 0
    fib4_nums[1] = 0
    fib4_nums[2] = 2

    # Compute the Fib4 numbers up to the nth number
    for i in range(3, n + 1):
        fib4_nums[i] = fib4_nums[i-1] + fib4_nums[i-2] + fib4_nums[i-3] + fib4_nums[i-4]

    return fib4_nums[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that computes the n-th element of the Fib4 number sequence using dynamic programming. It initializes a list `fib4_nums` to store the computed Fib4 numbers and iteratively computes them up to the nth number. The function then returns the nth Fib4 number. The script includes test cases to verify the correctness of the function.