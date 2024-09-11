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

    This function efficiently computes the n-th element of the fib4 number sequence
    using dynamic programming.
    """
    if n <= 3:
        # Base cases
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            return 0

    # Initialize array to store fib4 numbers
    fib4_numbers = [0, 0, 2, 0] + [0]*(n-3)

    # Compute fib4 numbers iteratively
    for i in range(4, n+1):
        fib4_numbers[i-1] = fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]

    # Return the n-th fib4 number
    return fib4_numbers[n-1]


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

In this script, we use dynamic programming to efficiently compute the n-th element of the fib4 number sequence. We initialize an array `fib4_numbers` to store the fib4 numbers up to the n-th element, and then we compute the fib4 numbers iteratively. The test cases at the end verify that the function works correctly.