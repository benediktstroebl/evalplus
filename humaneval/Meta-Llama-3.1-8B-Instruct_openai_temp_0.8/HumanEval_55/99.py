Here's a Python script that uses recursion to solve the Fibonacci problem efficiently using memoization.

```markdown
```python
def fib(n: int, memo={}):
    """
    Return n-th Fibonacci number using memoization.

    Args:
    n (int): The position of the Fibonacci number to be calculated.
    memo (dict, optional): Dictionary to store the Fibonacci numbers for memoization. Defaults to {}.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
        return result

# Example usage:
print(fib(10))
print(fib(1))
print(fib(8))
```

This script defines a recursive function `fib` that calculates the n-th Fibonacci number using memoization to achieve better performance. It raises an error if `n` is not a positive integer.
```

**Optimized Solution:**

For larger values of `n`, the above recursive solution can be inefficient due to redundant calculations. We can optimize it by using an iterative solution with a loop.

```markdown
```python
def fib(n: int):
    """
    Return n-th Fibonacci number using an iterative solution.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage:
print(fib(10))
print(fib(1))
print(fib(8))
```

This script defines an iterative function `fib` that calculates the n-th Fibonacci number using a loop, which is more efficient than the recursive solution for larger values of `n`.
```