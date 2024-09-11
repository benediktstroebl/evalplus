### Fibonacci Number Function
#### A Python Function to Calculate the nth Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

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

This Python function uses an iterative approach to calculate the nth Fibonacci number. It initializes two variables `a` and `b` with the first two Fibonacci numbers (1 and 1) and then iteratively calculates the next Fibonacci numbers by adding `a` and `b` and updating `a` and `b` accordingly. The function raises a `ValueError` if the input `n` is not a positive integer.