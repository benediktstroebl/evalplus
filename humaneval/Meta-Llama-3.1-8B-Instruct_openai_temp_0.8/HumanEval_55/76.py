### Fibonacci Number Calculation
#### Problem Description

The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.

#### Solution

Below is a Python function that calculates the n-th Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number.

    Example:
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
```

#### Explanation

This function uses an iterative approach to calculate the n-th Fibonacci number. It initializes two variables `a` and `b` to the first two Fibonacci numbers (1 and 1). Then, it iterates from the third Fibonacci number to the n-th Fibonacci number, updating `a` and `b` at each step. The final result is the n-th Fibonacci number stored in `b`.

Note that this function raises a `ValueError` if `n` is not a positive integer, as the Fibonacci sequence is not defined for non-positive integers.