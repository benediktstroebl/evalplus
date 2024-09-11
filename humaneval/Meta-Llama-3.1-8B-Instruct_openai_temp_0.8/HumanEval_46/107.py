### Fib4 Number Sequence Calculator

#### Overview
This script calculates the nth Fibonacci-like number in the Fib4 sequence efficiently using dynamic programming without recursion.

#### Code
```markdown
def fib4(n: int):
    """
    Calculates the nth Fibonacci-like number in the Fib4 sequence.

    The Fib4 number sequence is defined as follows:
    - fib4(0) = 0
    - fib4(1) = 0
    - fib4(2) = 2
    - fib4(3) = 0
    - fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    Args:
        n (int): The index of the Fibonacci-like number to calculate.

    Returns:
        int: The nth Fibonacci-like number in the Fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the Fibonacci-like numbers
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0

    # Calculate the Fibonacci-like numbers iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]

    return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

#### Explanation
The script first checks the base cases for the Fib4 sequence. Then, it initializes a list `fib4_sequence` to store the Fibonacci-like numbers. The list is initialized with the base cases and then the remaining Fibonacci-like numbers are calculated iteratively using a simple loop. Finally, the script returns the nth Fibonacci-like number in the Fib4 sequence.