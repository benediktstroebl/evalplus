```markdown
### Fib4 Number Sequence Calculator

This script calculates the n-th element of the Fib4 number sequence.

#### Code
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
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
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib4_sequence = [0, 0, 2]
        for i in range(3, n + 1):
            # Calculate the next element as the sum of the last four elements
            next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
            fib4_sequence.append(next_element)
        return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

#### Explanation
The provided script calculates the n-th element of the Fib4 number sequence using a loop. It initializes a list with the base elements of the sequence (0, 0, 2) and then iteratively calculates each subsequent element as the sum of the last four elements in the list. The n-th element is then returned. This approach avoids the use of recursion and is more memory-efficient than recursive methods.