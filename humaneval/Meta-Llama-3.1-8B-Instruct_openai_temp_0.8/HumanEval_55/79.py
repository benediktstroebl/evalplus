### Fibonacci Number Generator
#### A Python Script to Calculate the N-th Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
    n (int): The position of the Fibonacci number to be generated.

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


# Example usage
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script defines a recursive function `fib(n)` that calculates the n-th Fibonacci number. It uses the standard approach to Fibonacci sequence generation, where each number is the sum of the two preceding ones. The base cases are when `n` is 0 or 1, in which case the function returns `n` directly. For larger values of `n`, the function calls itself recursively to calculate the (n-1)th and (n-2)th Fibonacci numbers and sums them to get the nth number.

**Note:** This recursive approach can be inefficient for large values of `n` due to repeated calculations. A more efficient approach would be to use dynamic programming or memoization to store and reuse previously calculated values.