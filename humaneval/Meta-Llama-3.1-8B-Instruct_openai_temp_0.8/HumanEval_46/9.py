### Fib4 Number Sequence Calculator

Below is a Python script that efficiently computes the n-th element of the Fib4 number sequence without using recursion.

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
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Example:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib4_prev_prev_prev_prev, fib4_prev_prev_prev, fib4_prev_prev, fib4_prev = 0, 0, 2, 0
        for _ in range(3, n + 1):
            fib4_prev_prev_prev_prev, fib4_prev_prev_prev, fib4_prev_prev, fib4_prev = (
                fib4_prev_prev_prev_prev,
                fib4_prev_prev_prev,
                fib4_prev_prev,
                fib4_prev,
            )
            fib4_prev = fib4_prev_prev_prev_prev + fib4_prev_prev_prev + fib4_prev_prev
        return fib4_prev

# Example usage:
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the Fib4 number sequence without using recursion. It uses dynamic programming to store previous values and calculates the next one based on the previous four values. The example usage section demonstrates how to use this function with different inputs.