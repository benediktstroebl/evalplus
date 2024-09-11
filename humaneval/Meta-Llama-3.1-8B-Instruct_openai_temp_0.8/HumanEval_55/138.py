### Fibonacci Number Generator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to generate.

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
        return fib(n - 1) + fib(n - 2)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This script uses a recursive function to generate Fibonacci numbers. However, for larger values of `n`, this approach can be inefficient due to repeated calculations. A more efficient approach would be to use dynamic programming with memoization. Here's an updated version of the script:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to generate.

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
    memo = {0: 0, 1: 1}
    def fib_helper(k: int) -> int:
        if k not in memo:
            memo[k] = fib_helper(k - 1) + fib_helper(k - 2)
        return memo[k]
    return fib_helper(n)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This version uses a dictionary `memo` to store the Fibonacci numbers as they are calculated, eliminating the need for repeated calculations and making it more efficient for larger values of `n`.