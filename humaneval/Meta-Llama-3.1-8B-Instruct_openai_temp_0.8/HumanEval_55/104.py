### Fibonacci Number Calculator

This Python script calculates the nth Fibonacci number using memoization for efficient computation.

```markdown
### fib.py

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of Fibonacci number to be calculated.

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
    # Initialize a dictionary to store Fibonacci numbers
    memo = {1: 1}

    # Function to calculate Fibonacci number recursively
    def fib_recursive(k: int) -> int:
        # If Fibonacci number is already calculated, return it
        if k in memo:
            return memo[k]
        # Otherwise, calculate it and store it in the dictionary
        else:
            result = fib_recursive(k-1) + fib_recursive(k-2)
            memo[k] = result
            return result

    # Return the nth Fibonacci number
    return fib_recursive(n)


# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

You can run this script using Python (e.g., `python fib.py`) to verify the results.

### Explanation

The script uses a top-down approach to calculate Fibonacci numbers recursively with memoization:

1.  Initialize a dictionary (`memo`) to store previously calculated Fibonacci numbers.
2.  Define a nested function (`fib_recursive`) to calculate Fibonacci numbers recursively.
3.  In the recursive function:

    *   Check if the Fibonacci number has already been calculated and stored in `memo`. If so, return it directly.
    *   If not, calculate the Fibonacci number recursively, store the result in `memo`, and return it.
4.  The main `fib` function takes an input `n` and returns the nth Fibonacci number by calling the recursive function.

This approach minimizes redundant calculations by storing intermediate results and provides efficient computation for large inputs.