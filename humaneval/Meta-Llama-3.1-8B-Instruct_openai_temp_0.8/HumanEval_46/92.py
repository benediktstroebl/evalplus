### Efficient Fibonacci-like Sequence Calculation

Here's an efficient Python script to calculate the nth element of the Fib4 number sequence without using recursion.

```markdown
### fib4.py

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
    n (int): The position of the element in the sequence.

    Returns:
    int: The nth element of the Fib4 number sequence.
    """
    if n <= 3:
        # Base cases for Fib4 sequence
        return [0, 0, 2, 0][n]

    # Initialize the first four elements in the sequence
    fib4_sequence = [0, 0, 2, 0]

    # Calculate the sequence up to the nth element
    for i in range(4, n + 1):
        # Calculate the next element as the sum of the last four elements
        next_element = sum(fib4_sequence[-4:])
        fib4_sequence.append(next_element)

    # Return the nth element of the sequence
    return fib4_sequence[n]

# Test cases for the function
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

### Example Use Cases

To use this function, simply call it with the desired position `n` in the sequence as an argument, like this: `fib4(n)`. The function will return the nth element of the Fib4 number sequence.

You can also modify the function to handle different Fibonacci-like sequences by adjusting the base cases and the calculation of the next element in the sequence.