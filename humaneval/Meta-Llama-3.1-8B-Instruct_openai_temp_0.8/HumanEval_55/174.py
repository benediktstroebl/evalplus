### Fibonacci Number Generation
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # Base cases: F(1) = 1, F(2) = 1
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1

    # Initialize variables for dynamic programming
    a, b = 1, 1

    # Calculate F(n) iteratively
    for _ in range(2, n + 1):
        # Compute F(k+1) = F(k) + F(k-1)
        a, b = b, a + b

    return b


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This code implements an iterative solution to the Fibonacci problem using dynamic programming, which is more efficient for large values of `n`.