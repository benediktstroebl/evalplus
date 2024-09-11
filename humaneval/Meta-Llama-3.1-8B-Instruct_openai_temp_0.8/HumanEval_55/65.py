### Fibonacci Number Calculator
#### Python Script

```markdown
### Fibonacci Number Calculator

### Description
This Python script calculates the n-th Fibonacci number.

### Code

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    - n (int): Index of the Fibonacci number.

    Returns:
    - int: The n-th Fibonacci number.

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
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

### Explanation
The `fib` function uses a recursive approach to calculate the n-th Fibonacci number. If `n` is less than or equal to 1, it returns `n`. Otherwise, it calls itself with `n-1` and `n-2`, and returns the sum of these two numbers.

### Note
This recursive implementation has a high time complexity (O(2^n)) and may not be efficient for large values of `n`. For a more efficient solution, consider using an iterative approach or memoization.

### Run the Script
Save the script as `fibonacci.py` and run it using `python fibonacci.py` in your terminal.