### Fibonacci Number Generator
#### Using Memoization for Efficient Calculation

```python
def fib(n: int, memo={}):
    """
    Return n-th Fibonacci number.

    Args:
    - n: A non-negative integer.
    - memo: A dictionary used for memoization (default is an empty dictionary).

    Returns:
    - The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script uses a recursive function with memoization to efficiently calculate the n-th Fibonacci number. The `memo` dictionary stores previously calculated Fibonacci numbers to avoid redundant calculations. The function is designed to handle inputs up to 10, but it can be easily extended to larger inputs by changing the condition in the `if __name__ == "__main__":` block.