```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to return.

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

# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script uses an iterative approach to calculate the n-th Fibonacci number. It starts with `a` and `b` as 1, 1 and then iteratively updates them to be the last two numbers in the sequence. The time complexity of this approach is O(n), which is much more efficient than the recursive approach for large numbers.