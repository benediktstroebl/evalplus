### Fibonacci Number Calculation
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to calculate.

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

However, a more efficient solution would be to use memoization to store and reuse previous Fibonacci numbers, avoiding redundant calculations.

### Fibonacci Number Calculation with Memoization
```python
def fib(n: int, memo: dict = {}) -> int:
    """
    Return n-th Fibonacci number using memoization.

    Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to calculate.
        memo (dict): A dictionary to store previously calculated Fibonacci numbers.

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
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

Both scripts calculate the n-th Fibonacci number, but the second one uses memoization to optimize performance for large values of n.