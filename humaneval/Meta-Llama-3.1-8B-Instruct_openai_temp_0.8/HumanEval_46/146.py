### Self-Contained Python Script for Fib4 Number Sequence

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence 
    using an iterative approach.

    Args:
    n (int): The position of the element in the fib4 sequence.

    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n < 4:
        return 0

    a, b, c, d = 0, 0, 2, 0
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d


# Example usage:
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

This script defines the `fib4` function, which efficiently computes the n-th element of the Fib4 number sequence using an iterative approach. The function takes an integer `n` as input and returns the corresponding element in the sequence. The example usage at the end demonstrates how to use the `fib4` function to compute the first few elements of the sequence.