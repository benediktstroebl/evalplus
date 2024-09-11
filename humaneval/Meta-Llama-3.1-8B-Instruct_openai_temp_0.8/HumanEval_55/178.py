```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.

    Args:
        n (int): The position of the Fibonacci number to be found.

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
        return "Input should be a positive integer"
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

In this script, I have implemented the recursive approach to calculate the n-th Fibonacci number. The time complexity of this approach is O(n), making it efficient for small to moderate values of n. However, it may not be suitable for large values of n due to its recursive nature, which may lead to stack overflow. 

If you need to calculate large Fibonacci numbers, consider using an iterative approach or memoization to avoid recalculating the same Fibonacci numbers multiple times.