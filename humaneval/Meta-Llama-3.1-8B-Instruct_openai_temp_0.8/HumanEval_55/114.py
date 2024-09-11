```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number.

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


# Test the function
for i in range(1, 11):
    print(f"fib({i}) = {fib(i)}")
```

This script uses recursion to calculate the n-th Fibonacci number. However, please note that this recursive approach is not efficient for large values of `n` because it performs many redundant calculations.

To improve performance, you can use an iterative approach or memoization. Here's an example of memoization:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number.

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
    
    memo = {0: 0, 1: 1}  # base cases
    
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]


# Test the function
for i in range(1, 11):
    print(f"fib({i}) = {fib(i)}")
```

This version uses a dictionary to store the Fibonacci numbers as they are calculated, avoiding redundant calculations and improving performance.