### Fibonacci Number Calculator
#### Overview

This Python script provides a function `fib` that calculates the n-th Fibonacci number.

#### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.

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

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

#### Explanation

This script defines a recursive function `fib` that calculates the n-th Fibonacci number.

-   If `n` is less than or equal to 0, it raises a `ValueError`.
-   If `n` is 1 or 2, it returns 1, as the first and second Fibonacci numbers are 1.
-   For `n` greater than 2, it uses an iterative approach to calculate the n-th Fibonacci number. It initializes `a` and `b` with the first two Fibonacci numbers (1 and 1) and then updates them in each iteration until it reaches the n-th Fibonacci number.

The example usage at the end demonstrates how to use the `fib` function to calculate the 10th, 1st, and 8th Fibonacci numbers.