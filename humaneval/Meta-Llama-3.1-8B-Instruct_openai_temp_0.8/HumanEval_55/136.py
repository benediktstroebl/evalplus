### Fibonacci Number Calculation
#### Python Script
```markdown
## Fibonacci Function Implementation

Here is a Python function that calculates the nth Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Fibonacci sequence position.

    Returns:
    int: n-th Fibonacci number.

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


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

### Notes

- The above function uses recursion to calculate Fibonacci numbers. However, this approach is not efficient for large values of n.
- For larger values of n, consider using an iterative approach or memoization to optimize performance.

### Iterative Approach

Here's an iterative implementation of the Fibonacci function:

```python
def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    
    fib_prev = 0
    fib_curr = 1
    
    for _ in range(2, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr


# Example usage
print(fib_iterative(10))  # Output: 55
print(fib_iterative(1))   # Output: 1
print(fib_iterative(8))   # Output: 21
```

This iterative function has a time complexity of O(n) and uses a constant amount of extra space. It's suitable for calculating large Fibonacci numbers efficiently.