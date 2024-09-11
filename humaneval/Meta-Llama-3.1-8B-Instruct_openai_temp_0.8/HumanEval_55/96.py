```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to return.

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
    else:
        return fib(n-1) + fib(n-2)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines the `fib` function, which calculates the n-th Fibonacci number recursively. The function uses memoization to avoid redundant calculations, but in this simple version, each Fibonacci number is recalculated from scratch.

However, for larger values of n, this approach will be inefficient due to the repeated calculations involved in the recursive calls. 

Here is a more efficient version of the script using dynamic programming:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to return.

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
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i - 1] + fib_values[i - 2])
    return fib_values[n]


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This version of the script calculates and stores each Fibonacci number in a list as it's needed, rather than recalculating it each time. This makes the function much more efficient for large values of n.