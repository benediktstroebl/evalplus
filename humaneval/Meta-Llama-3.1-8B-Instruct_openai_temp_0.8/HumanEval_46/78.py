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
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    elif n <= 3:
        return {0: 0, 1: 0, 2: 2, 3: 0}[n]
    else:
        fib4_sequence = [0, 0, 2, 0]
        for i in range(4, n + 1):
            fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])
        return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a dictionary to store the first four elements of the sequence, and then uses a loop to calculate the remaining elements in the sequence. The time complexity of this script is O(n), which is much more efficient than the recursive approach, which has a time complexity of O(4^n).