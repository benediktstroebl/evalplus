```markdown
### Fibonacci Number Generator

This script provides a function to generate the nth Fibonacci number.
The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.

#### Code

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

#### Explanation

This function uses a recursive approach to calculate the nth Fibonacci number. However, it's not the most efficient method for large values of n because it performs many repeated calculations.

#### Optimized Version

If you need to calculate large Fibonacci numbers, consider using an iterative approach or memoization to avoid the repeated calculations.

```python
def fib(n: int) -> int:
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[n]
```

This optimized function uses a list to store the Fibonacci sequence and appends new numbers as necessary. It's a more efficient approach for large values of n.