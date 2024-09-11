### Fibonacci Number Generator
#### A Python Function to Calculate the nth Fibonacci Number

Below is a Python script that includes a function `fib(n)` to generate the nth Fibonacci number using memoization for efficient calculation.

```markdown
### Fibonacci Number Generator
#### A Python Function to Calculate the nth Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to generate.

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    # Base cases
    if n == 1:
        return 1
    elif n == 0:
        return 0

    # Create a dictionary to store the Fibonacci numbers
    memo = {0: 0, 1: 1}

    # Calculate the Fibonacci number using memoization
    for i in range(2, n + 1):
        # If the Fibonacci number is not in the dictionary, calculate it and add it
        memo[i] = memo[i - 1] + memo[i - 2]

    # Return the nth Fibonacci number
    return memo[n]
```

You can run this script in your Python environment to test the `fib(n)` function. This solution uses memoization to store the Fibonacci numbers as they are calculated, which significantly improves the performance for larger values of `n`.