```markdown
# Fib4 Number Sequence
=====================

This script calculates the nth element of the Fib4 number sequence.

### Code

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
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the Fib4 number sequence.
    """
    if n <= 3:
        fib4_sequence = [0, 0, 2]
    else:
        fib4_sequence = [0, 0, 2, 0]
        for i in range(4, n + 1):
            fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
    
    return fib4_sequence[n]

# Example usage
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

### Explanation

The `fib4` function takes an integer `n` as input and returns the nth element of the Fib4 number sequence. It uses dynamic programming to efficiently calculate the sequence up to the nth element.

If `n` is less than or equal to 3, it directly returns the corresponding element of the sequence. Otherwise, it initializes the sequence with the known elements and calculates the remaining elements up to the nth position using a loop.

The function returns the nth element of the sequence.

### Time Complexity

The time complexity of the `fib4` function is O(n), where n is the input position. This is because it uses a loop to calculate the sequence up to the nth element.

### Space Complexity

The space complexity of the `fib4` function is O(n), where n is the input position. This is because it stores the sequence up to the nth element in a list.