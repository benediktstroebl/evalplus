**Fibonacci Function**
=====================

The following Python script defines a recursive function to calculate the `n`-th Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to be calculated.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n  # Base cases: fib(0) = 0, fib(1) = 1
    else:
        return fib(n-1) + fib(n-2)  # Recursive case: fib(n) = fib(n-1) + fib(n-2)


# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

**Note:** This recursive implementation has an exponential time complexity due to the repeated calculation of the same Fibonacci numbers. For larger values of `n`, consider using an iterative approach or memoization to improve performance.

**Memoized Implementation**
---------------------------

If you prefer to use a memoized approach, consider the following modification:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to be calculated.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    memo = {0: 0, 1: 1}  # Store base cases in a dictionary

    def fib_helper(k: int) -> int:
        if k not in memo:  # If result is not cached
            memo[k] = fib_helper(k-1) + fib_helper(k-2)  # Calculate and store result
        return memo[k]

    return fib_helper(n)  # Use the helper function for calculation


# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This memoized version has a linear time complexity and is more efficient for larger values of `n`.