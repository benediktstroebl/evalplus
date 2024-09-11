### Self-Contained Python Script to Calculate Fib4 Number Sequence
```markdown
## Description
This Python script calculates the n-th element of the Fib4 number sequence.
The Fib4 sequence is defined as:
- fib4(0) = 0
- fib4(1) = 0
- fib4(2) = 2
- fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

## Usage
To use the script, save it to a file and run it from the command line:
```bash
python fib4.py
```
You can then call the `fib4(n)` function to calculate the n-th element of the Fib4 sequence.

## Code
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
    n (int): The index of the Fib4 number to calculate.

    Returns:
    int: The n-th element of the Fib4 number sequence.

    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib4_sequence = [0, 0, 2]
        while len(fib4_sequence) <= n:
            fib4_sequence.append(fib4_sequence[-1] + fib4_sequence[-2] + fib4_sequence[-3] + fib4_sequence[-4])
        return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script uses a simple iterative approach to calculate the n-th element of the Fib4 sequence. It initializes a list to store the sequence, and then iteratively appends new elements using the recursive formula. The function returns the n-th element of the sequence.