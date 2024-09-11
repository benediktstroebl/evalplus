### Fibonacci Number Calculator
#### Problem Description
The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.

#### Solution
```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
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

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
#### Explanation
The provided Python script implements a function `fib(n)` to calculate the `n-th` Fibonacci number. It uses an iterative approach for better performance compared to a recursive one. The function raises a `ValueError` for any negative input values of `n`, adhering to the requirement that the Fibonacci sequence starts from 0 and 1.