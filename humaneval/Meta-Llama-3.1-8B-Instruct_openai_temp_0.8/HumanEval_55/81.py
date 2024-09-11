```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci of {i} is: {fib(i)}")
```

This script calculates the `n`-th Fibonacci number using recursion. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

However, please note that this recursive approach has an exponential time complexity due to the repeated calculations of the same subproblems. For larger values of `n`, a more efficient approach using dynamic programming would be more suitable.

Here's an optimized version using dynamic programming:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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

    fib_sequence = [0] * (n + 1)
    fib_sequence[1] = 1

    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]

    return fib_sequence[n]


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci of {i} is: {fib(i)}")
```

In this optimized version, we store the Fibonacci numbers as we calculate them in a list `fib_sequence`, which allows us to look up previously computed values instead of recalculating them, resulting in a linear time complexity.