### Fibonacci Number Calculator
#### A Python Function to Calculate the N-th Fibonacci Number

Here's a Python script that uses dynamic programming to efficiently calculate the N-th Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]


# Example usage:
if __name__ == "__main__":
    print("10th Fibonacci number:", fib(10))
    print("1st Fibonacci number:", fib(1))
    print("8th Fibonacci number:", fib(8))
```

This function uses a dynamic programming approach to calculate Fibonacci numbers iteratively, which is more efficient than a recursive approach for larger values of `n`. The time complexity is O(n), making it suitable for large inputs.