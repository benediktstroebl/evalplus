```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Example usage
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
    try:
        print(fib(-5))
    except ValueError as e:
        print(e)  # Output: n must be a non-negative integer
```

Please note that this recursive solution is not efficient for large values of `n` due to the repeated computation of the same sub-problems. A more efficient solution would use dynamic programming to store and reuse previously computed values.

If you want an iterative solution or memoized recursive solution, let me know.