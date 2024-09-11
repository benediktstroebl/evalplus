### Fibonacci Number Calculator
#### Using Iterative Approach

Here's a Python script that calculates the n-th Fibonacci number using an iterative approach:
```python
def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

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

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This script defines a `fib` function that takes an integer `n` as input and returns the n-th Fibonacci number. It uses an iterative approach to calculate the Fibonacci sequence, which is more efficient than a recursive approach for large values of `n`.

The function first checks if `n` is less than or equal to 1, in which case it returns `n` directly. Otherwise, it initializes two variables `a` and `b` to 0 and 1, respectively, which represent the previous two numbers in the Fibonacci sequence. It then enters a loop that runs from 2 to `n` (inclusive), updating `a` and `b` in each iteration to the next two numbers in the sequence. Finally, it returns the last number in the sequence, which is the n-th Fibonacci number.