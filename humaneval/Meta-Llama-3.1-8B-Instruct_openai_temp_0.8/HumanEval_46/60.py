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
        n (int): The index of the Fib4 number sequence to compute.

    Returns:
        int: The nth element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the Fibonacci sequence
    fib_sequence = [0, 0, 2, 0]

    # Compute the Fibonacci sequence up to the nth element
    for i in range(4, n + 1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2] + fib_sequence[i-3] + fib_sequence[i-4])

    # Return the nth element of the Fibonacci sequence
    return fib_sequence[n]

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses an iterative approach to compute the Fib4 sequence up to the nth element. It initializes a list with the base cases, and then iteratively computes the subsequent elements of the sequence. Finally, it returns the nth element of the sequence.