### Fibonacci Number Generator
#### A Self-Contained Python Script

```markdown
### Usage
Run the script to test the `fib` function.

### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

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
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# Test cases
print(fib(10))   # Expected output: 55
print(fib(1))    # Expected output: 1
print(fib(8))    # Expected output: 21
```

### Explanation
This script uses recursive function calls to calculate the n-th Fibonacci number. The `fib` function checks if `n` is less than or equal to 1; if it is, it returns `n`. Otherwise, it calls itself with `n-1` and `n-2` as arguments, and returns the sum of the results.

**Please note:** While this solution is simple and easy to understand, it's not the most efficient way to calculate Fibonacci numbers for large `n`, as it does a lot of repeated computation. For larger values of `n`, you may want to use an iterative approach or a closed-form expression like Binet's formula.