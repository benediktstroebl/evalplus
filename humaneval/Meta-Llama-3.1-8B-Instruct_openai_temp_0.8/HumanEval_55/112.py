```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1.

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
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, this recursive solution has a major flaw - it does a lot of repeated work. For example, to calculate `fib(10)`, it needs to calculate `fib(9)` and `fib(8)`, and to calculate `fib(9)`, it needs to calculate `fib(8)` and `fib(7)`, so `fib(8)` is calculated twice.

This can be optimized by using a technique called memoization, which stores the results of expensive function calls and returns the cached result when the same inputs occur again.

Here's an optimized version of the function:

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    memo = {0: 0, 1: 1}  # Base cases

    def fib_helper(k):
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]

    return fib_helper(n)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

And here's an even more optimized version using a loop:

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b

    return b


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This version of the function has a time complexity of O(n), which is much more efficient than the original recursive solution for large values of n.