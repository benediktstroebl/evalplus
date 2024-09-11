### Fibonacci Number Generator
#### Problem Statement
Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. Here's a Python function to generate the n-th Fibonacci number.

#### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n: A positive integer representing the position of the Fibonacci number.

    Returns:
        An integer representing the n-th Fibonacci number.

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


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, this recursive approach can be inefficient for large inputs due to the repeated computation of the same Fibonacci numbers. A more efficient solution can be achieved using an iterative approach or memoization.

#### Memoized Version
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number using memoization.

    Args:
        n: A positive integer representing the position of the Fibonacci number.

    Returns:
        An integer representing the n-th Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    memo = {0: 0, 1: 1}
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This memoized version stores previously computed Fibonacci numbers in a dictionary to avoid redundant calculations and improve performance for larger inputs.