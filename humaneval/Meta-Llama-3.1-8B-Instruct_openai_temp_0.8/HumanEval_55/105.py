```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

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
        return n
    else:
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

Please note that this script uses a recursive approach which might not be efficient for large inputs due to repeated calculations. A more efficient solution would be to use dynamic programming or an iterative approach.

Here's an iterative version of the script:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

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
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This version of the script uses a loop to calculate the Fibonacci number, which is more efficient than the recursive version for large inputs.