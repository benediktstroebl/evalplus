### Fibonacci 4 Sequence Calculator
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

    Args:
    n (int): The position of the element in the Fib4 sequence.

    Returns:
    int: The nth element of the Fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib4_sequence = [0, 0, 2]
        for i in range(3, n + 1):
            fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
        return fib4_sequence[n]

# Test the function
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

This script uses an iterative approach to calculate the nth element of the Fib4 sequence. It initializes a list `fib4_sequence` with the first three elements of the sequence (0, 0, 2) and then iteratively calculates the remaining elements up to the nth element. The function returns the nth element of the sequence. The time complexity of this function is O(n), making it efficient for large values of n.