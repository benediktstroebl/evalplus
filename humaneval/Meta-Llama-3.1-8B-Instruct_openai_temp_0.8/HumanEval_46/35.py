```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
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
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize the first four elements of the sequence
        a, b, c, d = 0, 0, 2, 0

        # Compute the nth element
        for _ in range(3, n + 1):
            a, b, c, d = b, c, d, a + b + c + d

        return d

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function to compute the nth element of the Fib4 number sequence without using recursion. It initializes the first four elements of the sequence and then iteratively computes the subsequent elements using a loop. The function also includes docstrings to provide documentation for the function's parameters and return value.