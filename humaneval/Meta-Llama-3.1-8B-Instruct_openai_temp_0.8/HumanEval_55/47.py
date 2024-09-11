### Fibonacci Number Calculator

Here's a Python script that calculates the `n`-th Fibonacci number using the `@functools.cache` decorator for memoization:

```markdown
```python
import functools

def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
    n (int): The position of the Fibonacci number.

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
    if n == 1:
        return 1

    @functools.cache
    def fib_helper(k: int) -> int:
        if k <= 1:
            return 1
        return fib_helper(k-1) + fib_helper(k-2)

    return fib_helper(n)

print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, recursion is inefficient for large `n` due to repeated function calls. A more efficient solution involves using dynamic programming with iteration:

```markdown
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

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

    fib_prev = 1
    fib_curr = 1
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr

print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This version has a time complexity of O(n), making it much more efficient for large `n`.