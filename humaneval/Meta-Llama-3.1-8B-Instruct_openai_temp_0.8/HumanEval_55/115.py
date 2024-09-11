### Fibonacci Number Function
#### A Python Function to Calculate the nth Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1.

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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

### Explanation

*   The `fib` function takes an integer `n` as input and returns the `n`-th Fibonacci number.
*   It uses a loop to calculate the Fibonacci number iteratively, which is more efficient than a recursive approach.
*   The function raises a `ValueError` if `n` is not a positive integer.
*   The examples demonstrate the function's correctness by comparing its output with the expected results.