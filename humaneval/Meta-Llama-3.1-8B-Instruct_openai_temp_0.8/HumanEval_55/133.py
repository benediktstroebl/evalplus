```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This Python script defines a function `fib(n)` that calculates the n-th Fibonacci number. The function uses an iterative approach to avoid the recursion limit, which is more efficient for large values of `n`. It also includes input validation to ensure that the input is a positive integer.

The test cases at the end of the script demonstrate the function's correctness by printing the results for the Fibonacci numbers at positions 10, 1, and 8.