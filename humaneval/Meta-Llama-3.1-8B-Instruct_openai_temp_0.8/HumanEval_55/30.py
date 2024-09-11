### Fibonacci Number Calculation
#### Definition
The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1.

#### Python Implementation
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
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

#### Explanation
The `fib` function uses an iterative approach to calculate the n-th Fibonacci number. It initializes two variables `a` and `b` to the first two Fibonacci numbers, 1 and 1. Then, it iterates from 2 to `n`, updating `a` and `b` to the next two Fibonacci numbers in each iteration. Finally, it returns the n-th Fibonacci number, which is stored in `b`. The function raises a `ValueError` if `n` is not a positive integer.