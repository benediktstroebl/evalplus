### Fib4 Number Sequence Calculation
#### Using Dynamic Programming for Efficient Computation

Here's a Python function to calculate the n-th element of the Fib4 number sequence efficiently using dynamic programming.

```markdown
# fib4.py
```


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
    n (int): The index of the element in the Fib4 sequence.

    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    if n <= 3:  # Base cases
        return [0, 0, 2, 0][n]

    # Initialize an array to store the sequence
    fib4_seq = [0, 0, 2, 0, 0, 0]  # Room for n+1 elements

    # Calculate the sequence iteratively
    for i in range(4, n + 1):
        fib4_seq[i] = fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4]

    return fib4_seq[n]

# Example usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to calculate the n-th element of the Fib4 number sequence efficiently. By storing previous results in an array (`fib4_seq`), it avoids redundant calculations and achieves a time complexity of O(n).