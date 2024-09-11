### Fib4 Number Sequence
#### Efficient Computation of the n-th Element

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

    Args:
    n (int): The index of the element in the Fib4 sequence.

    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    if n < 2:
        return 0
    a, b, c, d = 0, 0, 2, 0
    for _ in range(2, n + 1):
        a, b, c, d = b, c, d, b + c + a + d
    return d

# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

This script uses a loop to efficiently compute the n-th element of the Fib4 sequence. It maintains a running total of the last four elements of the sequence (`a`, `b`, `c`, `d`), updating these values at each step of the loop. At the end of the loop, the value of `d` is the n-th element of the sequence. This approach avoids the overhead of recursive function calls, making it more efficient for large values of `n`.