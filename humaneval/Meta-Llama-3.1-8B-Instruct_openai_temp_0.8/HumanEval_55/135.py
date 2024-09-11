```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1. This function uses an iterative approach to calculate the n-th Fibonacci number.

    Args:
        n (int): Index of the Fibonacci number to be calculated.

    Returns:
        int: The n-th Fibonacci number.

    Example:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 1:
        return n  # Base cases
    else:
        fib_prev = 0
        fib_curr = 1
        for _ in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr


# Test cases
print(fib(10))  # Expected output: 55
print(fib(1))   # Expected output: 1
print(fib(8))   # Expected output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number using an iterative approach. It handles base cases where n is less than or equal to 1, and calculates the Fibonacci number for n greater than 1 using a loop. The test cases at the end demonstrate the function's correctness.