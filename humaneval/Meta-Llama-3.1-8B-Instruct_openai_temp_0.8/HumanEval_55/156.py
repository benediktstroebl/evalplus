```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
    n (int): The position of the Fibonacci number in the sequence.

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
        return "Input should be a positive integer."
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
print(fib(10))   # Output: 55
print(fib(1))    # Output: 1
print(fib(8))    # Output: 21
print(fib(0))    # Output: Input should be a positive integer.
print(fib(-1))   # Output: Input should be a positive integer.
print(fib(3))    # Output: 2
print(fib(2))    # Output: 1
```

This script uses a loop to calculate the n-th Fibonacci number, which is the recommended approach for large values of n because the recursive approach can cause a stack overflow. The function first checks for edge cases where n is less than or equal to 0 or equal to 1 or 2. If n is less than or equal to 0, it returns a message indicating that the input should be a positive integer. If n is 1 or 2, it returns 1. Otherwise, it uses a loop to calculate the n-th Fibonacci number.