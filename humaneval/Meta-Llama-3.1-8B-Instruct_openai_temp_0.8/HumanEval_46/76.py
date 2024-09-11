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
        n (int): The position of the element in the Fib4 sequence.

    Returns:
        int: The n-th element of the Fib4 sequence.
    """
    if n <= 1:
        return 0
    if n == 2:
        return 2
    fib4_sequence = [0, 0, 2] + [0]*(n-2)
    for i in range(3, n+1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    return fib4_sequence[n]


# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
print(fib4(10))  # Expected output: 56
```

This script defines a function `fib4(n)` that calculates the n-th element of the Fib4 sequence using dynamic programming. The function first checks for the base cases, then initializes a list to store the sequence. The list is populated using a loop, where each element is the sum of the four preceding elements. The function finally returns the n-th element of the sequence. The test cases at the end validate the function using the provided examples.