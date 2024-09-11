### Fibonacci Number Generator
#### Recursive Implementation

Here's a Python function that generates the `n`-th Fibonacci number recursively:
```markdown
### Fibonacci Number Generator

#### Recursive Implementation

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Index of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.
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

Please note that this recursive implementation is not efficient for large values of `n` due to the repeated computation of the same Fibonacci numbers. For larger inputs, consider using an iterative or memoized approach.

#### Iterative Implementation

Here's an iterative implementation of the Fibonacci function:
```markdown
#### Iterative Implementation

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Index of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This iterative implementation is more efficient than the recursive one, especially for large values of `n`, as it avoids the repeated computation of the same Fibonacci numbers.