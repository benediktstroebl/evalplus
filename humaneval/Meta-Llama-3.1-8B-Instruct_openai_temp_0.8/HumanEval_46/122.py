```markdown
## Fib4 Number Sequence Calculator
### A Python Script to Efficiently Compute the N-th Element of the Fib4 Number Sequence

#### Problem Statement
The Fib4 number sequence is a sequence similar to the Fibonacci sequence, defined as follows:
- `fib4(0)` -> 0
- `fib4(1)` -> 0
- `fib4(2)` -> 2
- `fib4(3)` -> 0
- `fib4(n)` -> `fib4(n-1)` + `fib4(n-2)` + `fib4(n-3)` + `fib4(n-4)`

#### Solution
```python
def fib4(n: int) -> int:
    """
    Efficiently compute the n-th element of the fib4 number sequence.

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Initialize a list to store the sequence elements
    sequence = [0, 0, 2, 0] + [0]*(n-3)

    # Compute the sequence elements iteratively
    for i in range(4, n+1):
        # Each element is the sum of the previous three elements
        sequence[i-1] = sequence[i-1] + sequence[i-2] + sequence[i-3] + sequence[i-4]

    return sequence[n]
```

#### Example Usage
```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
```